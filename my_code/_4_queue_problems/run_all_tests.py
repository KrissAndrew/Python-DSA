import sys
import os
import subprocess

# ✅ Ensure `my_code` is in Python's module path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

def run_tests():
    TESTS_DIR = os.path.dirname(os.path.abspath(__file__))  # Ensure correct directory
    print(f"📂 Searching in: {TESTS_DIR}")

    test_files = sorted(
        [f for f in os.listdir(TESTS_DIR) if f.startswith("_") and f.endswith(".py")]
    )

    print(f"📝 Found test files: {test_files}")

    if not test_files:
        print("❌ No test files found. Check your file paths and naming conventions.")
        return

    print("\n🚀 Running all tests...\n")

    for test in test_files:
        print(f"🟢 Running {test}...\n{'-'*40}")

        # ✅ Use UTF-8 to prevent encoding issues
        process = subprocess.run(
            ["python", os.path.join(TESTS_DIR, test)],
            env={**os.environ, "PYTHONUNBUFFERED": "1"},
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",  # ✅ Fix UnicodeDecodeError
            errors="replace"   # ✅ Replace problematic characters
        )

        print(process.stdout)  # ✅ Ensure test output is visible
        if process.stderr:
            print("❌ Error:\n", process.stderr)

    print("\n✅ All tests completed.\n")

if __name__ == "__main__":
    run_tests()
