import requests
import pandas as pd
from bs4 import BeautifulSoup
from utils import ROOT_DIR


# class with static methods to extract tables with one header from html to dataframe
class HTMLTableParser(object):
    # gets html from url, breaks content into table(s), returns as list
    @staticmethod
    def parse_url(url):
        html_response = requests.get(url)
        entire_html = BeautifulSoup(html_response.text, 'lxml')
        table_list = entire_html.find_all('table')
        return [HTMLTableParser.parse_table(table) for table in table_list]

    # break table into rows and columns
    @staticmethod
    def parse_table(table):
        n_columns = 0
        n_rows = 0
        column_names = []

        # iterate over all rows to configure table dimensions
        for row in table.find_all('tr'):
            td_tags = row.find_all('td')
            # adds row to table if td_tag has content
            if len(td_tags) > 0:
                n_rows += 1
                # set number of columns by finding the max number of columns in each row
                if n_columns == 0:
                    n_columns = len(td_tags)

        # get the table headers
        th_tags = table.find_all('th')
        if len(th_tags) > 0 and len(column_names) == 0:  # prevent repeats from being added
            for th in th_tags:
                column_names.append(th.getText())

        # ensure column names match number of columns
        if len(column_names) > 0 and len(column_names) != n_columns:
            raise Exception("Column names do not match number of columns, cannot generate table")

        data_frame_columns = column_names if len(column_names) > 0 else range(0, n_columns)
        output_df = pd.DataFrame(columns=data_frame_columns, index=range(0, n_rows))

        # add data to dataframe
        row_marker = 0  # index for rows
        for row in table.find_all('tr'):
            column_marker = 0  # index for columns
            columns = row.find_all('td')
            for column in columns:
                output_df.iat[row_marker, column_marker] = column.getText()
                column_marker += 1
            if len(columns) > 0:
                row_marker += 1

        # try to convert string to float
        for column in output_df:
            try:
                output_df[column] = output_df[column].astype(float)
            except ValueError:
                pass

        return output_df


# saves notes to frequency to music_note_mapper.csv
if __name__ == "__main__":
    note_frequency_url = 'https://pages.mtu.edu/~suits/notefreqs.html'
    list_of_df = HTMLTableParser.parse_url(note_frequency_url)

    file_path = f'{ROOT_DIR}\\data\\music_note_mapper.csv'
    list_of_df[1].to_csv(file_path, index=False)
