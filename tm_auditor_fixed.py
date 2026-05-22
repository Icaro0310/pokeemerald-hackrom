#!/usr/bin/env python3
"""
TM Auditor Fixed - Entende ambos os sistemas de nomes: ITEM_TM01 e ITEM_TM_FOCUS_PUNCH
"""

import re
import sys

ITEMS_FILE = "src/data/items.h"
TMS_HMS_FILE = "include/constants/tms_hms.h"

# Cores para terminal
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def get_tm_moves():
    """Extract TM moves from FOREACH_TM macro"""
    try:
        with open(TMS_HMS_FILE, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"ERROR: {TMS_HMS_FILE} not found!")
        sys.exit(1)

    match = re.search(r'#define FOREACH_TM\(F\)(.*?)#define FOREACH_HM', content, re.DOTALL)
    if not match:
        match = re.search(r'#define FOREACH_TM\(F\)(.*?)(?:#define|$)', content, re.DOTALL)

    if not match:
        print("ERROR: Could not find FOREACH_TM macro!")
        sys.exit(1)

    macro_body = match.group(1)
    moves = []
    for line in macro_body.split('\\'):
        m = re.search(r'F\(([^)]+)\)', line)
        if m:
            moves.append(m.group(1))
    return moves

def get_hm_moves():
    """Extract HM moves from FOREACH_HM macro"""
    try:
        with open(TMS_HMS_FILE, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return []

    match = re.search(r'#define FOREACH_HM\(F\)(.*?)(?:#define|$)', content, re.DOTALL)
    if not match:
        return []

    macro_body = match.group(1)
    moves = []
    for line in macro_body.split('\\'):
        m = re.search(r'F\(([^)]+)\)', line)
        if m:
            moves.append(m.group(1))
    return moves

def audit_items_h(tm_moves, hm_moves):
    """Audit items.h for all TM/HM blocks - entende ambos sistemas"""
    try:
        with open(ITEMS_FILE, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"ERROR: {ITEMS_FILE} not found!")
        sys.exit(1)

    total_tms = len(tm_moves)
    total_hms = len(hm_moves)

    print(f"\n{BLUE}=== TM/HM AUDIT REPORT (FIXED) ==={RESET}")
    print(f"FOREACH_TM macro: {total_tms} moves")
    print(f"FOREACH_HM macro: {total_hms} moves")
    print(f"TM 01-50: ITEM_TM_<MOVE_NAME> format")
    print(f"TM 51-100: ITEM_TM<NUMBER> format")
    print("=" * 60)

    # Check TMs 01-50 (usando ITEM_TM_<MOVE>)
    print(f"\n{BLUE}--- TMs 01-50 (ITEM_TM_<MOVE> format) ---{RESET}")

    ok_count = 0
    broken_count = 0
    missing_count = 0

    for i, move in enumerate(tm_moves[:50], start=1):
        # Sistema 1: ITEM_TM_<MOVE_NAME>
        item_name = f"ITEM_TM_{move}"
        
        # Find block
        pattern = r'\[' + item_name + r'\] =\s*\{(.*?)\},'
        match = re.search(pattern, content, re.DOTALL)

        if not match:
            print(f"{RED}[MISS]{RESET} TM{i:02d} ({move}): Block NOT FOUND in items.h")
            missing_count += 1
            continue

        block = match.group(1)
        issues = []

        # Check secondaryId
        sec_match = re.search(r'\.secondaryId\s*=\s*MOVE_(\w+)', block)
        if not sec_match:
            issues.append("no secondaryId")
        elif sec_match.group(1) == "NONE":
            issues.append("secondaryId=MOVE_NONE")
        elif sec_match.group(1) != move:
            issues.append(f"wrong move (got {sec_match.group(1)}, expected {move})")

        # Check description
        if "sQuestionMarksDesc" in block:
            issues.append("generic description")
        elif "COMPOUND_STRING" not in block:
            issues.append("no description")

        # Check price
        price_match = re.search(r'\.price\s*=\s*(\d+)', block)
        if price_match:
            price = int(price_match.group(1))
            if price == 1:
                issues.append(f"price={price}")
        else:
            issues.append("no price")

        # Check name shows correct TM number
        name_match = re.search(r'\.name\s*=_\("TM(\d+)"_', block)
        if name_match and int(name_match.group(1)) != i:
            issues.append(f"wrong TM number (shows TM{name_match.group(1)})")

        if issues:
            print(f"{RED}[BROKEN]{RESET} TM{i:02d} ({move}): {', '.join(issues)}")
            broken_count += 1
        else:
            print(f"{GREEN}[OK]{RESET} TM{i:02d} ({move})")
            ok_count += 1

    # Check TMs 51-100 (usando ITEM_TM<number>)
    print(f"\n{BLUE}--- TMs 51-100 (ITEM_TM<number> format) ---{RESET}")

    for i, move in enumerate(tm_moves[50:], start=51):
        # Sistema 2: ITEM_TM<number>
        item_name = f"ITEM_TM{i:02d}"
        
        # Find block
        pattern = r'\[' + item_name + r'\] =\s*\{(.*?)\},'
        match = re.search(pattern, content, re.DOTALL)

        if not match:
            print(f"{RED}[MISS]{RESET} TM{i:02d} ({move}): Block NOT FOUND in items.h")
            missing_count += 1
            continue

        block = match.group(1)
        issues = []

        # Check secondaryId
        sec_match = re.search(r'\.secondaryId\s*=\s*MOVE_(\w+)', block)
        if not sec_match:
            issues.append("no secondaryId")
        elif sec_match.group(1) == "NONE":
            issues.append("secondaryId=MOVE_NONE")
        elif sec_match.group(1) != move:
            issues.append(f"wrong move (got {sec_match.group(1)}, expected {move})")

        # Check description
        if "sQuestionMarksDesc" in block:
            issues.append("generic description")
        elif "COMPOUND_STRING" not in block:
            issues.append("no description")

        # Check price
        price_match = re.search(r'\.price\s*=\s*(\d+)', block)
        if price_match:
            price = int(price_match.group(1))
            if price == 1:
                issues.append(f"price={price}")
        else:
            issues.append("no price")

        # Check name shows correct TM number
        name_match = re.search(r'\.name\s*=_\("TM(\d+)"_', block)
        if name_match and int(name_match.group(1)) != i:
            issues.append(f"wrong TM number (shows TM{name_match.group(1)})")

        if issues:
            print(f"{RED}[BROKEN]{RESET} TM{i:02d} ({move}): {', '.join(issues)}")
            broken_count += 1
        else:
            print(f"{GREEN}[OK]{RESET} TM{i:02d} ({move})")
            ok_count += 1

    # Check HMs
    if total_hms > 0:
        print(f"\n{BLUE}--- HMs (01-{total_hms:02d}) ---{RESET}")
        for i, move in enumerate(hm_moves, start=1):
            # HMs usam ITEM_HM_<MOVE>
            item_name = f"ITEM_HM_{move}"
            pattern = r'\[' + item_name + r'\] =\s*\{(.*?)\},'
            match = re.search(pattern, content, re.DOTALL)

            if not match:
                print(f"{YELLOW}[MISS]{RESET} HM{i:02d} ({move}): Block NOT FOUND")
                continue

            block = match.group(1)
            issues = []

            sec_match = re.search(r'\.secondaryId\s*=\s*MOVE_(\w+)', block)
            if not sec_match or sec_match.group(1) == "NONE":
                issues.append("no valid secondaryId")

            if "sQuestionMarksDesc" in block:
                issues.append("generic description")

            if issues:
                print(f"{RED}[BROKEN]{RESET} HM{i:02d} ({move}): {', '.join(issues)}")
            else:
                print(f"{GREEN}[OK]{RESET} HM{i:02d} ({move})")

    # Check for extra TMs (beyond macro count)
    print(f"\n{BLUE}--- Extra TMs (beyond macro) ---{RESET}")
    extra_found = False
    for i in range(total_tms + 1, 151):
        item_name = f"ITEM_TM{i:02d}"
        if item_name in content:
            extra_found = True
            print(f"{YELLOW}[EXTRA]{RESET} {item_name} found in items.h but NOT in FOREACH_TM macro")
    if not extra_found:
        print("No extra TMs (101-150) found in items.h")

    # Summary
    print(f"\n{BLUE}=== SUMMARY ==={RESET}")
    print(f"Total TMs in macro: {total_tms}")
    print(f"{GREEN}OK: {ok_count}{RESET}")
    print(f"{RED}BROKEN: {broken_count}{RESET}")
    print(f"{RED}MISSING: {missing_count}{RESET}")

    if broken_count == 0 and missing_count == 0:
        print(f"\n{GREEN}All TMs are properly configured!{RESET}")
    else:
        print(f"\n{YELLOW}Some TMs need attention.{RESET}")

def main():
    print("pokeemerald-expansion TM/HM Auditor (Fixed)")
    print("=" * 60)

    tm_moves = get_tm_moves()
    hm_moves = get_hm_moves()
    audit_items_h(tm_moves, hm_moves)

if __name__ == "__main__":
    main()