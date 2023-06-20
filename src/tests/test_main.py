try:
    from .wow.test_widgets import run_tests as widgets_tests
    from .wow.test_detect import run_tests as detectr_tests
    from .wow.test_ypprpo import run_tests as windows_test

    windows_test()
    widgets_tests()
    detectr_tests()
except ImportError as err:
    print(f"Could't run GUI tests:\n {err}")
