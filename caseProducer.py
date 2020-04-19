import os
from excelReader import read_case_from_excel


def write_case_to_rf(rf_path, excel_path):
    case_collect = read_case_from_excel(excel_path)

    valid_cases_sum = 0
    for case_dir in case_collect:
        suite_path = f"{os.path.join(rf_path, case_dir)}.robot"
        suite_dir = os.path.dirname(suite_path)

        if not os.path.exists(suite_dir):
            os.makedirs(suite_dir)

        if os.path.exists(suite_path):
            with open(suite_path, mode="r", encoding="utf8") as f:
                suite_content = f.read()
        else:
            suite_content = "***Test Case***\n"

        for case_name, case_desc in case_collect[case_dir].items():
            if case_name not in suite_content:
                suite_content += f"{case_name}\n{case_desc}\n"
                valid_cases_sum += 1
        with open(suite_path, mode="w", encoding="utf8") as f:
            f.write(suite_content)

    all_cases_sum = sum([len(cases) for cases in case_collect.values()])
    print(f"共添加{valid_cases_sum}个有效用例, 略过{all_cases_sum - valid_cases_sum}个已存在用例")


def main():
    rf = "E:/MyRepository/robotframework-testcase-generator/rf_project_demo/CaseSet"
    excel = "E:/MyRepository/robotframework-testcase-generator/TestCase.xls"
    write_case_to_rf(rf, excel)


if __name__ == '__main__':
    main()
