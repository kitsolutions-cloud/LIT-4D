# DEPRECATED: This test script is deprecated and will be removed in a future release.
# Use the `tasks` package instead: python -m tasks
import sys
import os
from unittest.mock import patch, MagicMock

# Add scripts directory to path so we can import automations
scripts_dir = os.path.dirname(os.path.abspath(__file__))
if scripts_dir not in sys.path:
    sys.path.insert(0, scripts_dir)

import automations

# Mock providers for testing logic
mock_func1 = MagicMock()
mock_func2 = MagicMock()
automations.PROVIDERS = {
    "provider1": {"func1": mock_func1},
    "provider2": {"func1": mock_func2, "func2": MagicMock()}
}

def test_run_all():
    print("Testing run all (no -p argument)...")
    mock_func1.reset_mock()
    mock_func2.reset_mock()
    # Mocking sys.argv to simulate calling: python scripts/automations.py -f func1
    with patch('sys.argv', ['automations.py', '-f', 'func1']):
        try:
            automations.main()
        except SystemExit:
            pass
    
    assert mock_func1.called, "mock_func1 should have been called"
    assert mock_func2.called, "mock_func2 should have been called"
    print("Test run all passed!")

def test_run_single():
    print("Testing run single (-p provider1)...")
    mock_func1.reset_mock()
    mock_func2.reset_mock()
    # Mocking sys.argv to simulate calling: python scripts/automations.py -p provider1 -f func1
    with patch('sys.argv', ['automations.py', '-p', 'provider1', '-f', 'func1']):
        try:
            automations.main()
        except SystemExit:
            pass
    
    assert mock_func1.called, "mock_func1 should have been called"
    assert not mock_func2.called, "mock_func2 should NOT have been called"
    print("Test run single passed!")

def test_not_found():
    print("Testing function not found error handling...")
    # Mocking sys.argv to simulate calling: python scripts/automations.py -f nonexistent
    with patch('sys.argv', ['automations.py', '-f', 'nonexistent']):
        try:
            automations.main()
        except SystemExit as e:
            assert e.code == 1, f"Expected exit code 1, got {e.code}"
    print("Test function not found passed!")

if __name__ == "__main__":
    try:
        test_run_all()
        test_run_single()
        test_not_found()
        print("\nAll tests passed successfully!")
    except AssertionError as e:
        print(f"\nTest failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred during testing: {e}")
        sys.exit(1)
