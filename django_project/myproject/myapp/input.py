
import geopandas as gpd
shppath = "/Users/yaswanthi.otra/Desktop/Point_4888_UID_2/point_4888_UID_2.shp"
gdf = gpd.read_file(shppath)
import psycopg2

df1 = gdf[['OBJECTID' ,'SyncID', 'FeatureNam','FeatureSta','UniqueID','RouteID','RouteName','RouteCla','MaintCnt','Division']]
print(df1)


try:
    connection = psycopg2.connect(user="postgres",
                                  password="yaswanthi",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="my_db")
    cursor = connection.cursor()

    for i in range(11 , 101):
        postgres_insert_query= """ INSERT INTO myapp_Asset1 (object_id ,asset_id, asset_name, asset_stat,segment_id,route_id,route_name,route_class,county_id,division_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        record_to_insert = (int(df1.OBJECTID[i]) , str(df1.SyncID[i]), str(df1.FeatureNam[i]), str(df1.FeatureSta[i]),str(df1.UniqueID[i]),str(df1.RouteID[i]),str(df1.RouteName[i]),str(df1.RouteCla[i]),str(df1.MaintCnt[i]),str(df1.Division[i]))
        cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)