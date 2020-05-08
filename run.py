from tools.os import shell_tool
import pytest
                                                                                           
if __name__ == '__main__':
    # 修改成要执行的测试用例
    test_case2 = './test_case/user/test_lianxi1.py'
    #test_case2 = './test_case/user/test_lianxi1.py'

    xml_report_path = './reports/xml/'
    html_report_path = './reports/html/'

    pytest.main(['-s', '-q', '--alluredir',
                 xml_report_path, test_case2])
    cmd1 = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    cmd2 = 'allure serve %s' % (xml_report_path)

    shell_tool.invoke(cmd1)
    shell_tool.invoke(cmd2)
