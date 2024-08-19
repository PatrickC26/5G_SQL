import 5G_SQL_library
coon = 5G_SQL_library._5G_SQL(host="192.168.100.10",user="pi",passwd="raspberry", databaseName="exampledb", debug=True)
coon.getALL("test")
conn.getALL("ee716")
conn.getALL("test", "id")
#
conn.getColumns("test", "id")
conn.getColumns("test", ["id", "email"])
conn.getColumns("test", "email", "id")
conn.getColumns("test", ["name", "email"], "id")
conn.getColumns("test", columnNames=["id", "name", "email"], orderBy="id")
#
conn.insert("test", ["id", "email", "name", "no", "date"], [0, "fd", "sdferferfjio", 8934, 908])
#
conn.addColumn("test", "date", "int")
#
conn.updateData("test", ["id"], [80])
conn.updateData("test", ["id", "name"], [8, "iouh"])
conn.updateData("test", ["name"], ["sdfsdfdsf"], ["id", "date"], [8, 0])
conn.updateData(tableName="test", ["email", "name"], ["sfdsfQff.off", "iouh"], ["id"], [540])
conn.updateData("test", ["name"], ["iouh"], ["date"], [908])
conn.updateData("test", ["id", "name"], [540, "iouh"], ["date"], [908])
#
conn.deleteColumn("test", "date")
#
conn.clearTable("test")
