import os
import xlrd

from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, timeline, is_platform_windows

def get_icloudReturnsAcc(files_found, report_folder, seeker, wrap_text):
    
    for file_found in files_found:
        file_found = str(file_found)
        filename = os.path.basename(file_found)
        
        if filename.startswith('~'):
            continue
        if filename.startswith('.'):
            continue
        
        loc = file_found
        
        
        dth = []
        list = []
        data_headers = []
        data_list =[]
        
        #First worksheet
        
        wb = xlrd.open_workbook(loc)
        sheetnames = wb.sheet_names() 
        sheet = wb.sheet_by_index(0)
        dsid = sheet.cell_value(2, 0)
        
        for i in range(sheet.nrows):
            for j in range(sheet.ncols):
                if i == 6:
                    dth.append(sheet.cell_value(i, j))
                if i >= 7:
                    list.append(sheet.cell_value(i, j))
            if i >= 7:
                data_list.append(list) 
            list =[]
        
        
        if data_list:
            description = f'Sheet name: {sheetnames[0]} - {dsid}'
            report = ArtifactHtmlReport('iCloud - Account Details')
            report.start_artifact_report(report_folder, 'iCloud - Account Details', description)
            report.add_script()
            data_headers = (dth)
            report.write_artifact_data_table(data_headers, data_list, file_found)
            report.end_artifact_report()
            
        else:
            logfunc('No iCloud - Account Details data available')
            
        #Second worksheet
        dth = []
        list = []
        data_headers = []
        data_list =[]
        
        wb = xlrd.open_workbook(loc)
        sheetnames = wb.sheet_names() 
        
        sheet = wb.sheet_by_index(1)
        dsid = sheet.cell_value(2, 0)
        
        for i in range(sheet.nrows):
            for j in range(sheet.ncols):
                if i == 5:
                    dth.append(sheet.cell_value(i, j))
                if i >= 6:
                    list.append(sheet.cell_value(i, j))
            if i >= 6:
                data_list.append(list) 
            list =[]
            
            
        if data_list:
            description = f'Sheet name: {sheetnames[1]} - {dsid}'
            report = ArtifactHtmlReport('iCloud - Account Features')
            report.start_artifact_report(report_folder, 'iCloud - Account Features', description)
            report.add_script()
            data_headers = (dth)
            report.write_artifact_data_table(data_headers, data_list, file_found)
            report.end_artifact_report()
            
        else:
            logfunc('No iCloud - Account Features data available')
            
__artifacts__ = {
        "icloudReturnsAcc": (
            "iCloud Returns",
            ('*/Account/*_AccountDetails.xlsx'),
            get_icloudReturnsAcc)
}