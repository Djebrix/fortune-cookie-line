import os

FORTUNE = "A stranger will ask you to write their wedding vows. You will nail them, and still take the blame at the divorce."

def main():
    assert 1 <= len(FORTUNE) <= 140, "fortune must be 1-140 characters"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(FORTUNE)

if __name__ == "__main__":
    main()
