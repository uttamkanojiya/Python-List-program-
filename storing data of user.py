#program for practice
row1=['🔴','🟠','🟡']
row2=['🟢','🔵','🟣']
row3=['⚫️','⚪️','🟤']
matrix=[row1,row2,row3]
print(f'{row1}\n{row2}\n{row3}')
postion=(input('enter the postion where you want to hide money'))
row_number=int(postion[0])
column_number=int(postion[1])
row_selected=matrix[row_number-1]
row_selected[column_number-1]='❎ '
print(f'{row1}\n{row2}\n{row3}')

