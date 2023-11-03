# pytest的主入口
import os
import time
import pytest

if __name__ == '__main__':
    pytest.main()

    time.sleep(3)
    os.system('allure generate ./result -o ./test-reports --clean')