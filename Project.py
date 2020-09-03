import pandas as pd
import matplotlib.pyplot as plt

class calUtils:
        def visit(self):
                dict = {"country": ['Brunei','Indonesia','Malaysia','Philippines','Thailand','Vietnam' ,'Myanmar','Japan', 'Hong Kong', 'China', 'Taiwan', " Korea, Republic Of ", 'India', 'Pakistan',
                                    'Sri Lanka', 'Saudi Arabia', 'Kuwait', 'UAE'],
                        "num": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
                        "sums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]}

                df = pd.DataFrame(dict, columns=['country', 'num', 'sums'])
                df2 = pd.read_csv('IMVA.csv')

                dff = df2[[' Brunei Darussalam ', ' Indonesia ',' Malaysia ',' Philippines ',' Thailand ', ' Viet Nam ',' Myanmar ',' Japan ',' Hong Kong ',' Taiwan ', ' China ', " Korea, Republic Of ",' India ', ' Pakistan ',' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE ']].head(120)
                print(dff)

                if dff[' Brunei Darussalam '].dtypes == object:
                        df['sums'] = df['sums'].replace(1, 0)

                if dff[ ' Indonesia '].dtypes == object:
                        df['sums'] = df['sums'].replace(2, 0)

                if dff[' Malaysia '].dtypes == object:
                        df['sums'] = df['sums'].replace(3, 0)

                if dff[' Philippines '].dtypes == object:
                        df['sums'] = df['sums'].replace(4, 0)

                if dff[' Thailand '].dtypes == object:
                        df['sums'] = df['sums'].replace(5, 0)

                if dff[' Viet Nam '].dtypes == object:
                        df['sums'] = df['sums'].replace(6, 0)

                if dff[' Myanmar '].dtypes == object:
                        df['sums'] = df['sums'].replace(7, 0)

                if dff[' Japan '].dtypes == object:
                        df['sums'] = df['sums'].replace(8,0)

                if dff[' Hong Kong '].dtypes == object:
                        df['sums'] = df['sums'].replace(9,0)

                if dff[' China '].dtypes == object:
                        df['sums'] = df['sums'].replace(10,0)

                if dff[' Taiwan '].dtypes == object:
                        df['sums'] = df['sums'].replace(11,0)

                if dff[" Korea, Republic Of "].dtypes == object:
                        df['sums'] = df['sums'].replace(12,0)

                if dff[' India '].dtypes == object:
                        df['sums'] = df['sums'].replace(13,0)

                if dff[' Pakistan '].dtypes == object:
                        df['sums'] = df['sums'].replace(14,0)

                if dff[' Sri Lanka '].dtypes == object:
                        df['sums'] = df['sums'].replace(15,0)

                if dff[' Saudi Arabia '].dtypes == object:
                        df['sums'] = df['sums'].replace(16,0)

                if dff[' Kuwait '].dtypes == object:
                        df['sums'] = df['sums'].replace(17,0)

                if dff[' UAE '].dtypes == object:
                        df['sums'] = df['sums'].replace(18,0)

                japan = dff[' Japan '].sum()
                hk = dff[' Hong Kong '].sum()
                china = dff[' China '].sum()
                twn = dff[' Taiwan '].sum()
                kr = dff[" Korea, Republic Of "].sum()
                ind = dff[" India "].sum()
                pakistan = dff[" Pakistan "].sum()
                srilanka = dff[" Sri Lanka "].sum()
                saudiarabia = dff[" Saudi Arabia "].sum()
                kuwait = dff[" Kuwait "].sum()
                uae = dff[" UAE "].sum()

                df['sums'] = df['sums'].replace(1,0)
                df['sums'] = df['sums'].replace(2,0)
                df['sums'] = df['sums'].replace(3,0)
                df['sums'] = df['sums'].replace(4,0)
                df['sums'] = df['sums'].replace(5,0)
                df['sums'] = df['sums'].replace(6,0)
                df['sums'] = df['sums'].replace(7,0)
                df['sums'] = df['sums'].replace(8, japan)
                df['sums'] = df['sums'].replace(9, hk)
                df['sums'] = df['sums'].replace(10, china)
                df['sums'] = df['sums'].replace(11, twn)
                df['sums'] = df['sums'].replace(12, kr)
                df['sums'] = df['sums'].replace(13, ind)
                df['sums'] = df['sums'].replace(14, pakistan)
                df['sums'] = df['sums'].replace(15, srilanka)
                df['sums'] = df['sums'].replace(16, saudiarabia)
                df['sums'] = df['sums'].replace(17, kuwait)
                df['sums'] = df['sums'].replace(18, uae)
                print(df)

                df.sort_values(by=['sums'], inplace=True, ascending=False)
                df.reset_index(drop=True, inplace=True)

                newdf = df.nlargest(3,'sums')
                print(newdf)
                df['countries'] = df['country']
                df.index = df["country"]
                del df["num"]
                del df["country"]
                print(df)
                #Top 3 bar chart
                ax = newdf.plot(kind='bar', x='country', y='sums', title="Number of Visitors in Countries",
                        ylabel="Number of Tourists (in millions) ", rot=0, legend=False, figsize=(15, 15))
                for p in ax.patches:
                        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
                plt.savefig("scatterDiagram_Top3.png")
                #plt.show()

                # all countries bar chart
                ax = df.plot(kind='bar',x='countries',y='sums',title="Number of Visitors in Countries",
                        ylabel="Number of Tourists (in millions) ",rot=45, legend=False, figsize=(25,25))
                for p in ax.patches:
                        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
                plt.savefig("Country_comparison.png")
                #plt.show()



j = calUtils()
j.visit()