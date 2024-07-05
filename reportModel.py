import pandas as pd
import numpy as np
import datetime
import os
import glob

class dailyReport():
    def __init__(self, combined_xls):
        self.combined_xls = combined_xls
        self.storeName = ''
        self.combined_xls = self.combined_xls.astype({'入库数量':int, '出库数量':int})
        self.df_in = self.combined_xls.groupby(['店铺', '相关单号', '作业类型名称'])['入库数量'].sum().reset_index()
        self.df_in = self.df_in[self.df_in.入库数量 != 0]
        self.df_out = self.combined_xls.groupby(['店铺', '相关单号', '作业类型名称'])['出库数量'].sum().reset_index()
        self.df_out = self.df_out[self.df_out.出库数量 != 0]

    def get_storeName(self, report_name):
        self.report_name = report_name
        if self.report_name == 'Columbia':
            self.storeName= 'Columbia HK Brand Store'
        elif self.report_name == 'MBO商城':
            self.storeName = 'MBO官方商城'
        elif self.report_name == 'NBA':
            self.storeName = 'NBA香港官方商城'
        elif self.report_name == 'Nike.com':
            self.storeName = '香港NIKE官方商城'
        elif self.report_name == 'Puma':
            self.storeName = 'Puma Hong Kong Brand Site 店铺'
        elif self.report_name == 'Microsoft':
            self.storeName ='微软香港官方商城'
        elif self.report_name == 'Adidas':
            self.storeName = 'AdidasHK官方商城'
        elif self.report_name == 'Reebok':
            self.storeName = 'ReebokHK官方商城'

    def get_stockinbound(self):
        return self.df_in.入库数量.where((self.df_in.店铺 == self.storeName) & (self.df_in.作业类型名称 == 'VMI移库入库')).sum().astype(int) + self.df_in.入库数量.where((self.df_in.店铺 == self.storeName) & (self.df_in.作业类型名称 == '采购入库')).sum().astype(int)
       
    def get_saleQty(self):    
        return self.df_out.出库数量.where((self.df_out.店铺 == self.storeName) & (self.df_out.作业类型名称 == '销售出库')).sum().astype(int) + self.df_out.出库数量.where((self.df_out.店铺 == self.storeName) & (self.df_out.作业类型名称 == '退换货出库')).sum().astype(int)

    def get_saleOrder(self): 
        return self.df_out.店铺.where((self.df_out.店铺 == self.storeName) & (self.df_out.作业类型名称 == '销售出库')).count() + self.df_out.店铺.where((self.df_out.店铺 == self.storeName) & (self.df_out.作业类型名称 == '退换货出库')).count()
        
    def get_returnOrder(self):    
        return self.df_in.店铺.where((self.df_in.店铺 == self.storeName) & (self.df_in.作业类型名称 == '退换货入库')).count()

    def get_returnQty(self):
        return self.df_in.入库数量.where((self.df_in.店铺 == self.storeName) & (self.df_in.作业类型名称 == '退换货入库')).sum().astype(int)
        
    def get_vmiReturn(self):
        return self.df_out.出库数量.where((self.df_out.店铺 == self.storeName) & (self.df_out.作业类型名称 == 'VMI转店退仓出库')).sum().astype(int)