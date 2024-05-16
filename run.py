
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import wx
import pandas as pd
import datetime
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg


from MainTemplate import MainScreen
from VisualisationTemplate import Visualisation
EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'
df = pd.read_csv("test.csv",index_col=0)
class DataTable(wx.grid.GridTableBase):
    def __init__(self, data=None):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 1
        self.data = data

    def GetNumberRows(self):
        return len(self.data.index)

    def GetNumberCols(self):
        return len(self.data.columns)

    def GetValue(self, row, col):
        return self.data.iloc[row, col]

    def SetValue(self, row, col, value):
        self.data.iloc[row, col] = value

    # For better visualisation
    def GetColLabelValue(self, col):
        return self.data.columns[col]

    def GetAttr(self, row, col, prop):
        attr = wx.grid.GridCellAttr()
        if row % 2 == 1:
            attr.SetBackgroundColour(EVEN_ROW_COLOUR)
        return attr

    def GetColumnValues(self, column_name):
        # Get the index of the column with the specified name
        col_index = self.data.columns.get_loc(column_name)

        # Return the values in that column
        return self.data.iloc[:, col_index].unique().tolist()

class ReportFrame(MainScreen):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.table = None
        self.selected_region = None
        self.regionList.Bind(wx.EVT_COMBOBOX, self.region_list)  # Bind to the region_list function
        self.Show(True)
        self.Layout()
    def load_data( self, event ):
        self.table = DataTable(df)
        self.regionListChoices = df['REGION_NAME'].unique()
        self.regionList.Set(self.regionListChoices)
        self.dataTable.SetTable(self.table, takeOwnership=True)
        self.dataTable.AutoSize()
        self.m_panel151.Layout()
        self.Layout()

    def export_report(self, event):
        if self.table is not None:
            # Ask the user for a file name
            with wx.FileDialog(self, "Save CSV file", wildcard="CSV files (*.csv)|*.csv",
                               style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
                if fileDialog.ShowModal() == wx.ID_CANCEL:
                    return  # The user canceled the dialog

                # Proceed with saving
                file_path = fileDialog.GetPath()

                # Save the table data to the CSV file
                self.table.data.to_csv(file_path, index=False)

                wx.MessageBox(f"Exported as {file_path}", "Export Successful", wx.OK | wx.ICON_INFORMATION)

        else:
            wx.MessageBox("No data to export. Please load data first.", "Export Error", wx.OK | wx.ICON_ERROR)


    def search(self, event):
        keyword = self.searchbox.GetValue()

        if keyword:
            # Filter the data based on the ACCIDENT_TYPE column
            filtered_data = df[df['ACCIDENT_TYPE'].str.contains(keyword, case=False, na=False)]
            self.update_data_table(filtered_data)
        else:
            # If the search box is empty, show all data
            self.update_data_table(df)

    def update_data_table(self, data):
        # Clear the existing data from the data table
        self.dataTable.ClearGrid()

        # Populate the data table with the filtered data
        self.table = DataTable(data)
        self.dataTable.SetTable(self.table, takeOwnership=True)
        self.dataTable.AutoSize()
        self.m_panel151.Layout()
        self.Layout()

    def region_list(self, event):

        selected_region = self.regionList.GetValue()
        # Now, 'selected_region' contains the value selected by the user in the ComboBox
        self.selected_region = selected_region

    import datetime

    import datetime

    def apply_filter(self, event):
        start_date_wx = self.startDateBox.GetValue()
        end_date_wx = self.endDateBox.GetValue()
        # Convert wx.DateTime to datetime
        start_date = datetime.datetime(start_date_wx.GetYear(), start_date_wx.GetMonth() + 1, start_date_wx.GetDay())
        end_date = datetime.datetime(end_date_wx.GetYear(), end_date_wx.GetMonth() + 1, end_date_wx.GetDay())

        if self.selected_region is not None:
            # Filter the DataFrame based on selected region
            filtered_df = df[df['REGION_NAME'] == self.selected_region].copy()
            filtered_df['ACCIDENT_DATE'] = pd.to_datetime(filtered_df['ACCIDENT_DATE'], format='%d/%m/%Y')

            # Apply date filter
            filtered_df = filtered_df[
                (filtered_df['ACCIDENT_DATE'] >= start_date) & (filtered_df['ACCIDENT_DATE'] <= end_date)]
        else:
            filtered_df = df.copy()
            filtered_df['ACCIDENT_DATE'] = pd.to_datetime(filtered_df['ACCIDENT_DATE'], format='%d/%m/%Y')
            # Apply date filter
            filtered_df = filtered_df[
                (filtered_df['ACCIDENT_DATE'] >= start_date) & (filtered_df['ACCIDENT_DATE'] <= end_date)]


        # Update the table with the filtered data
        self.update_data_table(filtered_df)

    def go_visual(self, event):
        visual = VisualFrame(parent=self, table=self.table)
        visual.Show()
        self.Layout()


class VisualFrame(Visualisation):
    def __init__(self, parent=None, table=None):
        super().__init__(parent)
        self.table = table
        self.x = None
        self.y = None
        self.selected_chart = None
        column_names = [self.table.GetColLabelValue(col) for col in range(self.table.GetNumberCols())]
        self.xVariableChoices = column_names
        self.xVariable.Set(self.xVariableChoices)
        self.yVariableChoices = ['Accident Count']
        self.yVariable.Set(self.yVariableChoices)
        self.chartTypeChoices = ['Bar Chart', 'Column Chart', 'Pie Chart', 'Line Chart']
        self.chartType.Set(self.chartTypeChoices)
        self.Show(True)
        self.Layout()

    def load_data(self, event):
        self.table = DataTable(df)
        self.Refresh()
        self.Layout()

    def x_variable(self, event):
        x = self.xVariable.GetValue()
        self.x = x
    def y_variable(self, event):
        y = self.yVariable.GetValue()
        self.y = y

    def chart_type(self, event):
        selected_chart = self.chartType.GetValue()
        self.selected_chart = selected_chart

    def apply_visual_filter(self, event):
        figure_score = self.plot_data_line()
        h, w = self.visual_panel.GetSize()
        figure_score.set_size_inches(h / figure_score.get_dpi(), w / figure_score.get_dpi())

        canvas = FigureCanvasWxAgg(self.visual_panel, -1, figure_score)
        canvas.SetSize(self.visual_panel.GetSize())

        self.Layout()

    def plot_data_line(self):
        x = self.table.GetColumnValues(self.x)
        y = self.table.data[self.x].value_counts().tolist()
        figure_score = Figure()
        axes = figure_score.add_axes([0.1, 0.1, 0.8, 0.8])  # [left, bottom, width, height]

        if self.selected_chart == 'Bar Chart':
            axes.barh(x, y)
            axes.set_yticks(axes.get_yticks())
            axes.set_yticklabels(axes.get_yticklabels(), rotation=45, fontdict={'fontsize': 6})
            axes.set_ylabel('The number of accident')

        elif self.selected_chart == 'Column Chart':
            axes.bar(x, y)
            axes.set_xticks(axes.get_xticks())
            axes.set_xticklabels(axes.get_xticklabels(), fontdict={'fontsize': 6})
            axes.set_xlabel(self.x)  # Set xlabel instead of ylabel
            axes.set_ylabel('The number of accident')

        elif self.selected_chart == 'Line Chart':
            axes.plot(x, y)
            axes.set_xticks(axes.get_xticks())
            axes.set_xticklabels(axes.get_xticklabels(), fontdict={'fontsize': 6})
            axes.set_xlabel(self.x)  # Set xlabel instead of ylabel
            axes.set_ylabel('The number of accident')

        elif self.selected_chart == 'Pie Chart':
            axes.pie(y, labels=x, autopct='%1.1f%%')

        axes.set_title(self.title.GetValue())

        return figure_score

    def back_main(self, event):
        # Assuming self is a wx.Frame
        self.Close()

    def export_report(self, event):
        # Create a PDF file
        pdf_filename = "output.pdf"

        # Get the Matplotlib Figure from the canvas
        figure_score = self.plot_data_line()  # Assuming this returns the Matplotlib Figure

        # Save the Figure as a PDF
        figure_score.savefig(pdf_filename, format='pdf')

        wx.MessageBox(f"Exported as {pdf_filename}", "Export Successful", wx.OK | wx.ICON_INFORMATION)


if __name__ == "__main__":

    app = wx.App(False)
    frame = ReportFrame()
    app.MainLoop()
