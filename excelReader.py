import os
import xlrd
import json
from operator import eq


def read_case_from_excel(excel_path):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open("excel_config.json", mode="r", encoding="utf8") as f:
        config = json.load(f)

    wb = xlrd.open_workbook(excel_path)
    if config.get("caseSheet") not in wb.sheet_names():
        raise ValueError("找不到excel下对应的sheet页, 请在excel_config.json配置", config.get("caseSheet"))
    ws = wb.sheet_by_name(config.get("caseSheet"))
    case_path, case_no, case_title = config["casePath"], config["caseNo"], config["caseTitle"]
    case_prepare, case_step, case_expect = config["casePrep"], config["caseStep"], config.get("caseExpt")

    _1st_case_row = 1
    for row in range(ws.nrows):
        if eq(ws.cell_value(row, 0), case_path):
            _1st_case_row = row + 1
    cn_row = ws.row_values(_1st_case_row - 1)
    path_col, no_col, title_col, prep_col, step_col, expt_col = cn_row.index(case_path), cn_row.index(
        case_no), cn_row.index(case_title), cn_row.index(case_prepare), cn_row.index(case_step), cn_row.index(
        case_expect)

    cases_collect = {}
    """
    {
        "case_dir1": {
            "case_name1": "case_desc1",
            "case_name2": "case_desc2",
            ...
        },
        ...
    }
    """
    for row in range(_1st_case_row, ws.nrows):
        if ws.cell_value(row, 0) is None:
            continue
        case_dir = ws.cell_value(row, path_col).replace("\\", "/").strip("/")
        case_name = f"{ws.cell_value(row, no_col)}_{ws.cell_value(row, title_col)}"
        case_desc = combine_case_desc(ws.cell_value(row, prep_col), ws.cell_value(row, step_col),
                                      ws.cell_value(row, expt_col))
        if case_dir not in cases_collect.keys():
            cases_collect.update({case_dir: {case_name: case_desc}})
        elif case_name not in cases_collect[case_dir].keys():
            cases_collect[case_dir].update({case_name: case_desc})
    return cases_collect


def combine_case_desc(case_prepare, case_step, case_expect):
    header, gap = "    [Documentation]    ", "    ...    "
    case_prepare = case_prepare.replace('\n', f'\n{gap}')
    case_step = case_step.replace('\n', f'\n{gap}')
    case_expect = case_expect.replace('\n', f'\n{gap}')
    case_desc = f"{header}【前置条件】:\n" \
                f"{gap}{case_prepare}\n" \
                f"{gap}【用例步骤】:\n" \
                f"{gap}{case_step}\n" \
                f"{gap}【预期结果】:\n" \
                f"{gap}{case_expect}\n"
    return case_desc
