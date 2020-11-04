from enum import IntEnum

Menu_Values = IntEnum('Menu_Values', 'Value1 Value2 Value3 Value4 Value5')

select = input("""Menu pick:
1
2
3
4
5
""")

if select == Menu_Values.Value1:
    pass
elif select == Menu_Values.Value2:
    pass
elif select == Menu_Values.Value3:
    pass
elif select == Menu_Values.Value4:
    pass
elif select == Menu_Values.Value5:
    pass
