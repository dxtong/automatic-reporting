import pandas as pd
import numpy as np
import datetime
import os
import glob
from reportModel import *

class autogenReport():
    def autogen(self):
        all_filenames = [i for i in glob.glob('temp/' + datetime.datetime.now().strftime('%Y%m%d') +'*Log.xls')]
        combined_xls = pd.concat([pd.read_excel(f) for f in all_filenames ])

        df_report = pd.DataFrame(index=np.arange(13), columns=['日期', '类型            店铺', 'Columbia', 'MBO 商城', 'NBA', '微軟', 'Nike', 'Puma','Adidas', 'Reebok'])
        df_report = df_report.fillna(0)
        df_report.日期 = datetime.datetime.now().strftime("%Y/%m/%d")
        df_report['类型            店铺'] = ['收货上架','拣货','发货','取消单','发货异常单','退货入库订单数','退货入库件数','无指令','問題件','等待指令过仓','退货订单不符','轉店 / 退倉','盤點']

        report = dailyReport(combined_xls)
        reportStore = ['Columbia', 'MBO商城', 'NBA', 'Microsoft', 'Nike.com', 'Puma', 'Adidas', 'Reebok']
        reportNum = []

        for i in range(2, 10):
            reportNum.append(i)

        for j, k in zip(reportNum, reportStore):
            report.get_storeName(k)
            df_report.iloc[0,j] = report.get_stockinbound()

        for j, k in zip(reportNum, reportStore):
            report.get_storeName(k)
            df_report.iloc[1,j] = report.get_saleQty()

        for j, k in zip(reportNum, reportStore):
            report.get_storeName(k)
            df_report.iloc[2,j] = report.get_saleOrder()

        for j, k in zip(reportNum, reportStore):
            report.get_storeName(k)
            df_report.iloc[5,j] = report.get_returnOrder()

        for j, k in zip(reportNum, reportStore):
            report.get_storeName(k)
            df_report.iloc[6,j] = report.get_returnQty()

        for j, k in zip(reportNum, reportStore):
            report.get_storeName(k)
            df_report.iloc[11,j] = report.get_vmiReturn()

        df_report = df_report.drop(columns=['微軟', 'Nike', 'Puma', 'Adidas', 'Reebok'])
        df_report['TTL'] = df_report.sum(axis = 1)
        df_report = df_report.set_index(['日期', '类型            店铺'])
        self.df_report = df_report
        return self.df_report