try:
    from .wow.test_widgets import run_tests as widgets_tests
    from .wow.test_detect import run_tests as detectr_tests

    widgets_tests()
    detectr_tests()
except ImportError as err:
    print(f"Could't run GUI tests:\n {err}")
