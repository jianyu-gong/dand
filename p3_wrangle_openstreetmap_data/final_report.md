# OpenStreetMap Data Case Study
#### Author: Jianyu Gong
#### Date:  June 1st, 2017

### Map Area
Toronto, Ontario, Canada
I choose Toronto as my study area because I am currently living in Toronto and I am trying to find a job in Toronto. Therefore, it is good to know about the map information in Toronto. After auditing and cleaning data, we can query the information quickly in the future.

### Problems Encountered in the Map
The street names, postal codes and phone are audited by using audit.py. Several problems are found and presented as below.
The correct street name format should be ‘John Street East’, ‘Dundas Street’, ‘Jarvis Street’ and ‘Winston Churchill Boulevard’. The street address format problems are shown below:
- Over-abbreviated street names: (e.g. ‘John St E’ to ‘John Street East’)
- Inconsistent street names: (e.g. ‘Dundas street’ to ‘Dundas Street’, ‘JARVIS STREET’ to ‘Jarvis Street’)
- Wrong spelling: (e.g. ‘Winston Churchill Boulevade to ‘Winston Churchill Boulevard’)

The correct Canadian postal codes format should be A1A 1A1, where A is a capital letter and 1 is an integer. The postal code format auditing results and problems are summarized below: 

```python
The incorrect postcodes are: ['M6P4A9', 'L9T0R3', 'M5A2K7', 'L7M4A6', 'L7M4A5', 'L7M4A7', 'L7M4A5', 'L7M4A5', 'M4L1H6', 'M4E1g1', 'M5A1Z9', 'M5A1Z9', 'M5A1Z9', 'M5B2H1', 'M4G4B5', 'L5B2C9', 'L6Y0B8', 'L5M1L4', 'M1P0B1', 'M36 0H7', 'M6H4A9', 'L5M1L9', 'M6S4W6', 'M9C5H5', 'L6Y0M2', 'L7A2G8', 'L4H2J2', 'M5V1R1', 'L6S0B8', 'L6S0B8', 'n3r 5l8', 'm4x 1a6', 'M4L3G8', 'L7G4S4', 'L4W1V5', 'L6X1M9', 'l6c2t2', 'M1W3E6', 'm3j 2n7', 'L7A2X6', 'L0G1T0', 'L5M5K5', 'L5B1B6', 'L5H1G6', 'L5J1J6', 'L4S2N5', 'L5V2X8', 'L5R4G6', 'L5V3B7', 'L5T0A4', 'M5V1R1', 'M5H1X6', 'M4L1J2', 'M5T2G7', 'L5M6J3', 'L5G1H9', 'L7M4B8', '96734', 'L4G1Z8', 'M6C1C6', 'L4W2P7', 'M5E1E3', 'L4W1V5', 'L0G1W0', 'L5G1E2', 'M8W1R2', 'M8W1R2', 'L5L3R8', 'L4Y1A6', 'L7N4X7', 'L6Z1Y4', 'L6Z3S4', 'L6H7B8', 'L4X2X1', 'M8W1P9', 'M8V1J2', 'M8W3T7', 'L5G1H9', 'L6Z0E3', 'L6K3Y6', 'L6Z4R3', 'l7a 3r9', 'L5E1E6', 'L7K0A1', 'L1H7K5', 'M8Z1N5', 'M8Z1N7', 'L5W0E6', 'L4V1E1', 
'L9W2Z1', 'L5G4S6', 'L9P1P7', 'L9P1B4', 'L5J1J7', 'L5J1J5', 'L7K0W7', 'L7K0Y3', 'L9W5K1', 'L7C1M3', 'M8W1N5', 'M8W1N2', 'L5E1E3', 'L5E1E5', 'L5G1H3', 'L5G1H3', 'M8V1K5', 'M8V1K5', 'M8V1K5', 'M4S3G1', 'L5J1J4', 'L4W1K3', 'M6G3N1', 'L6T2W8', 'L9T2R3', 'L4Y1A6', 'L6R1T4', 'L6R1T4', 'L6X1M9', 'L6X1M8', 'L6V1N6', 'L4W1S9', 'L1V2W8', 'L5S1X7', 'L5V0B7', 'L5J1J5', 'L6P3A3', 'M5T3K7', 'L6E0K9', 'L6E0K9', 'M3C2E7', 'M3C2E6', 'M3C2E7', 'M4L1H9', 'M4L1J2', 'M2N 6k7', 'M5T2E7', 'L5J1K5', 'L7P3N8', 'L6L5B3', 'L6R1W4', 'M6S1N7', 'L6T4W2', 'L5J4S8', 'L4Y2B8', 'L4Z1N5', 'L4Z1P3', 'L6R0E1', 'L6R0M5', 'M5E', 'M5A2L1', 'L7M', 'L5N6A3', 'M8W1N6', 'M6R2K3', 'M5A1T2', 'L4J8A4', 'L4J8A4', 'L4J8A4', 'L4J8A4', 'L4J8A4', 'L4J8A4', 'L4J8A4', 'L4J8A4', 'L7G3T1', 'L6H2R9', 'L4K', 'L4W4Y5', 'M2J5B5', 'L7E4Z7', 'L9W1K2', 'M8W1N2', 'L0R', 'M5X2A1', 'L4K0A2', 'L1R0H5', 'M3J3H6', 'M3J1N2', 'M8W3T5', 'L5N1P7', 'L0R2H5', '14174', 'L5G1H4', 'M8V1L4', 'L6S0C6', 'L4W4V8', 'L3T2A5', 'ON L5G 4V6', 'L9G2C1', 'L0N1M0', 'L7K0Y3', 'l3Y 3J2', 'L6r Oj6', 'M8Y1J2', 'M8Y1J3', 'L4X2W7', 'L9W5N9', 'L5H2C4', 'M8W2B3', 'l3Y 3J2', 'L7T2B9', 'M8W1P4', 'L4X1L9', 'L4X1L9', 'L4X1L9', 'L5A3V9', 'L6J3J1', 'L5C1C3', 'L4Z3K8', 'L5A1W8', 'L7L1C7', 'M4E1g1', 'M4l1j1', 'M4E1g3', 'L5K1R8', 'L0G1A0', 'M1c 2z2', 'M4C1K9', 'M5A2L1', 'M4Y1Y9', 'M5E1E3', 'M9W1J8', 'l8h 1t8', 'L7E1C1', 'L6R1T4', 'M3M2J2', 'L6S0C6', 'M4E1H8', 'L3T6L2', 'L1N8Y9', 'M4S1S3', 'L6W2E1', 'M4K2R6', 'B2Y4N4', 'L4w4M6', 'L4w4M6', 
'M6N5G4', 'M5R1B9', 'L4Z1H8', 'L1H', 'L4W2R1', 'L4W1E9', 'L5N7Y5', 'M5G1H1', 'M5G0B2', 'L4W5A6', 'L5C3Y8', 'M2J', 'L0G1M0', 'L6Y1N7', 'L6R1W7', 'L6T3R5', 'L6R3S9', 'L6W2B5', 'L6S3Y5', 'L6Z2S6', 'L6P2Z8', 'L6V1N2', 'M2J4T1', 'L0G1T0', 'L6W0B4', 'M6P4A9', 'L6C1K8', 'M6J1G3', 'L4W1J1', 'L4W4M1', 'M1W3Y1', 'M1W3Y1', 'M1W3Y1', 'M2H1V9', 'L7M4B8', 'M9M2G3', 'M9M2G3', 'M9M2G3', 'M9M2G3', 'm9b1b6', 'L6L5B5', 'L6L5B3', 'L9V0N2', 'L3Y', 'M2N 6k7', 'M5T1A5', 'M4BS26', 'M4B2S6', 'M6A2T9', 'L4S1P3', 'L4S1P3', 'L4S1P3', 'L4S1P3', 'L4S1P3', 'L4S1P3', 'L6R1T4', 'L6R1T4', 'L6R1T4', 'L6R1T4', 'L6R1T4', 'L6R1T4', 'L6R1T4', 'L6R1T4', 'L6R1T4', 'L6R1T4', 'L6R1T4', 'L6R1T4', 'L6R1T4', 'L6R1T4', 'L6R1T4', 'L3Y3Z3', 'L0S1J0', 'L4C5E2', 'M5A1A6', 'M9W5T1', 'M5G1P7', 'L4Z3V5', 'M1W3E6', 'M1P3J3', 'm3L 2h9', 'M3J1V6', 'M9R', 'L5E3G2', 'M1H1S2', 'M6L3E2', 'M6L3E2', 'M6M4N8', 'L5V2B8', 'L5l2r4', 'L5L5Z5', 'L6V4K2', 'L6V4K2', 'L4Y2C2', 'L1W3R2', 'M1P3E9', 'L4X1L9', 'M1J2G4', 'L3R5B4', 'L5V2N6', 'L5V2N6', 'L6W4P5', 'L0G1T0', 'L4Z1W7', 'L6Z3M1', 'L4W4L8', 'L5T1X3', 'L4W2Z7', 'L4W1V2', 'L4W4G1', 'L4W5G6', 'L4W5M4', 'L5C2V1', 'L4V1T2', 'L4X2E2', 'L67 0A7', 'M8V3Z2', 'M9C', 'L7P2H5', 'L7P1S9', '33913', 'L6T5P9', 
'L4W2B9', 'L4S1P3', 'L4C6Z1', 'L4C5E2', 'L1S4S4', 'L5J1J7', 'M8Z1T8', 'L4Y2C1', 'L4Y2C5', 'L4X2Z3', 'L4X1L5', 'L4X2X1', 'M9C5H5', 'M8Z2G9', 'M8Z2G9', 'M8Z1T8', 'M8Z1R6', 'L9W6Z1', 'L9W3J8', 'M8Z2Z4', 'M8Z2Z8', 'M8Z2R4', 'M8Z5G8', 'M4S1A5', 'M4S1A5', 'L5W1L9', 'L3Y4X2', 'L3Y4X2', 'L5E1E2', 'L5E1E4', 'M9C4Z6', 'M9A3V3', 'M9C1V7', 'L5B1B5', 'M6K', 'L5M0H1', 'L6P1E7', 'L7A2Z3', 'L8T1J4', 'M8V1H5', 'M4L1J2', 'L5G1E9', 'L5C3P5', 'L9&5M3', 'L4Y1Y6', 'L6M4E2', 'M4S1S3', 'M6N4Z5', 'M5J 2G', 'L4B', 'N4X2P9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A6', 'L7M4A9', 'L7M4A6', 'L7M4A6', 'L7M4A6', 'L7M4A6', 'L7M4A6', 'L7M4A6', 'L7M4A6', 'L7M4A6', 'L7M4A6', 'L7M4A6', 'L7M4A6', 'L7M4A6', 'L7M4A9', 'L7M4A9', 'L7M4A6', 'L7M4A9', 'L7M4A6', 'L7M4A9', 'L7M4A6', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A6', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L7M4A9', 'L1W3Z7', 'L1W3Z7', 'L1W3Z7', 'L1W3Z7', 'L1W3Z6', 'L1W3Z7', 'L1W3Z7', 'L1W3Z7', 'L1W3Z7', 'L1W3Z7', 'L1W3Z7', 'L1W3Z7', 'L1W3Z7', 'L1W3Z7', 'L1W3Z7', 'L1W3Z7', 'L1W3Z7', 'L1W3Z7', 'L1W3Z7', 'L1W3Z7', 'M9W7K7', 'M4S1A5', 'L6X0B3', 'L3Y4X2', 'L3Y4X2', 'L8W1C4', 'L7K0X4', 'M8V1K2', 'L9L1P5', 'L6H7G6', 'L6J7R4', 'M8W1R2', 'M2J0A7', 'L6T0E2', 'L5W1L9', 'L5G1H3', 'L5G1H3', 'L5G1G8', 'L5G1H4', 'M4G1V7', 'M5B1L4', 'L6T2W8', 'L6P2S4', 'L6R3G2', 'L6P1W3', 'M4L1J2', 'L3R2A2', 'L6R0J9', 'M4M2M6', 
'M4M2M6', 'L6P2R1', 'l6p 2r1', 'L6R0W9', 'L5V2N6', 'L5H3B1', 'M8X1A9', 'M8X1A9', 'M2N1N1', 'L9T6N2', 'L5L4X5', 'L6P2S5', 'M6B3T4', 'L5C1Y2', 'L5A1B2', 'L5A2P1', 'L5A1S2', 'L0P1B0', 'L7K0A1', 'M9C3S6', 'M5V1V1', 'M9C1A8', 'L7C1X1', 'L4X1L4', 'L5H1G8', 'L5H1E9', 'L6S4B4', 'N1H6H9', 'L9T2X5', '14174-1003', '14174-1003', 'L6Z3L5', 'L6Z3L5', 'L6Z3L5', 'L6Z3L5', 'L6Z3L5', 'L9T7M4', 'L5G1G1', 'L7J 2', 'M6S2K3', 'L7L5H9', 'L6H7G5', 'L8M2K9', 'L4G7C6', 'M8W3W2', 'M1B5N6', 'M8X1M3', 'L6Y0Y3', 'L7K0E7', 'L5G1H9', 'L7K0W9', 'M9C1A8', 'M8X1P9', 'M8X1P9', 'M8X1P9', 'M8X1P9', 'L9T2T1', 'L9T2G5', 'L4W3Z3', 'L4H0A8', 'L5N7L7', 'L5V2N6', 'L5T2V8', 'L5G3R2', 'L5G3R2', 'L7A3Z6', 'L7A3Z6', 'L6X0S1', 'L4W4T4', 'L0G1A0', 'M1R4B9', 'm2l 2k4', 'M1k0a4', 'L7G2S4', 'M6B3S9', 'L3R2G9', 'M1R2R9', 'L1K0S1', 'm1g2l6', 'L1R3L7', 'M2K1C3', 'L5N2L8', 'L7E0W1', 'M6E4Y2', 'M6B3T1', 'M6B3T1', 'L3X 1KI3', 'M1W', 'M1W3w5', 'M1W3w5', 'M1W3w5', 'M1W3w5', 'M1W3w5', 'M1W3w5', 'M1W3w5', 'M1W', 'M1W', 'M1W3X6', 'M1W3X6', 'M1W3X6', 'M1W3X6', 'M1W3X6', 'M1W3T5', 'M1W3T5', 'M1W3T5', 'M1W3T5', 'M1W3T5', 'M1W3T5', 'M1W3T5', 'M1W3T5', 'M6B3S7', 'M6B3T2', 'M6E2Y8', 'L6R3S9', 'l8g 3p1', 'L6k2G3', 'L3Y3T3', 'M2N', 'L6Y0M4', 'L7L7J8', 'M6L3E2', 'M6L3E2', 'M6L3E2', 'L6H6M2', 'M8V0B8', 'M8V0B8', 'M8V0B8', 'M8V0B8', 'M8V0B8', 'M6E 28V']
```
- Incomplete postal codes: (e.g. ‘M5E’, ‘L3Y’)
- Some letters are lower case: (e.g. ‘l6p 2r1’, ‘m3j 2n7’)
- No blank space in middle: (e.g. ‘M4E1g1’, ‘M1k0a4’, ‘M5A2K7’)
-	Wrong Canadian postal format: (e.g. ‘14174-1003’, ‘ON L5G 4V6’)

After updating postal code, the postal codes containing lower case are changed to upper case and a space is added for the postal codes without blank space in middle.

### OpenStreetMap Results
#### 1. Sizes of the files
‘get_file_size.py’ is used to check the size of the file and the results are shown below:
```python
File Sizes:
toronto_canada.osm: 1.13455281314 GB
toronto.db: 851.45703125 MB
nodes.csv: 393.182883263 MB
nodes_tags.csv: 84.5013751984 MB
ways.csv: 41.6892700195 MB
ways_nodes.csv: 129.061340332 MB
ways_tags.csv: 91.1999101639 MB
```
#### 2. Count Tags
‘Count_tags’ in ‘audit,py’ is used to count the occurrences of each tag, and the results are shown below:
```python
{'node': 5065357, 'nd': 5797115, 'bounds': 1, 'member': 147130, 'tag': 4983486, 'relation': 9539, 'way': 752171, 'osm': 1}
```

#### 3. Number of Unique Users
```sql
sqlite> SELECT COUNT(DISTINCT(uid)) FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM Ways);
```
```2628```

#### 4. American Area
According to last section, some postcodes containing purely numbers. Therefore, it is considered as American area. The postcodes - ‘96734’, ‘14174’ – are checked:
```sql
SELECT id FROM nodes WHERE id IN (SELECT DISTINCT(id) FROM Nodetags WHERE key = 'postcode' and value = '96734');
```
```sql
1547753193
```
```sql
SELECT id FROM nodes WHERE id IN (SELECT DISTINCT(id) FROM Nodetags WHERE key = 'postcode' and value = '14174');
```
```sql
3443667462
```
```sql 
SELECT * FROM NodesTags WHERE id = "1547753193";
```
```sql
1547753193|city|Kailua|addr
1547753193|housenumber|1320 Aulepe|addr
1547753193|postcode|96734|addr
1547753193|province|HI|addr
1547753193|street|St #4|addr
```
```sql
SELECT * FROM NodesTags WHERE id = "3443667462";
```
```sql
3443667462|building|house|regular
3443667462|city|Youngstown|addr
3443667462|state|NY|addr
3443667462|street|Woodland|Court|addr
3443667462|postcode|14174|addr
3443667462|housenumber|451|addr
```
After checking the Google Maps, the 1320 Aulepe Street, Kailua, HI is located in Hawaiian Islands and 451 Woodland Court, Youngstwon, NY is on the Canada-US border. Therefore, those two data should be deleted from database.
```sql
sqlite> DELETE FROM nodes WHERE id = "3443667462";
sqlite> DELETE FROM nodes WHERE id = "1547753193";
sqlite> DELETE FROM NodesTags WHERE id = "3443667462";
sqlite> DELETE FROM NodesTags WHERE id = "1547753193";
```
#### 5. Number of Nodes
```sql
sqlite> SELECT COUNT(*) FROM nodes;
```
```5065357```
#### 6. Number of Ways
```sql
sqlite> SELECT COUNT(*) FROM Ways;
```
```752171```
#### 7. Top Five Contributing Users
```sql
sqlite> SELECT user, count(*) as num
   ...> FROM (SELECT user FROM nodes UNION ALL SELECT user FROM Ways)
   ...> GROUP BY user
   ...> ORDER BY num DESC
   ...> LIMIT 5;
```
```sql
andrewpmk|3389940
Kevo|484991
MikeyCarter|474443
Bootprint|209105
Victor Bielawski|142924
```
#### 8. Top Five Amenity
```sql
sqlite> SELECT value, count(*) as num
   ...> FROM NodesTags
   ...> WHERE key = "amenity"
   ...> GROUP BY value
   ...> ORDER BY num DESC
   ...> LIMIT 5;
```
```sql
fast_food|3124
restaurant|2961
bench|2409
post_box|2032
cafe|1459
```
#### 9. How Many Tim Hortons in Toronto Area?
```sql
sqlite> SELECT COUNT(*) FROM NodesTags WHERE value = "Tim Hortons";
```
```461```
#### 10. Top Five Cuisines
```sql
sqlite> SELECT value, COUNT(*) as num
   ...> FROM NodesTags
   ...> JOIN (SELECT DISTINCT(id) FROM NodesTags WHERE value = "restaurant") i 
   ...> ON NodesTags.id = i.id
   ...> WHERE NodesTags.key = 'cuisine'
   ...> GROUP BY NodesTags.value
   ...> ORDER BY num DESC
   ...> LIMIT 5;
```
```sql
chinese|163
indian|104
japanese|93
italian|90
pizza|65
```
### Additional Suggestions
```sql
sqlite> SELECT COUNT(*) FROM Nodestags WHERE key = "amenity";
```
```
26947
```
```sql
sqlite> SELECT COUNT(*) FROM NodesTags WHERE key = "wheelchair";
```
```sql
3743
```
During the investigation, the wheelchair accessible amenity is not enough. According to the query, the total number of amenity is 26947 and the total number of wheelchair accessible amenity is 3743 which is only 12.5% of all amenities. The low percentage of wheelchair accessible amenity maybe caused by incomplete information. The missing information can be found on various websites such as www.accessto.ca. That information can be updated through Python or manually. After updating, the percentage should be increased.
### Conclusion
The OpenStreetMap project is challenging. Data wrangling skill, data cleaning skill as well as SQL knowledge are practiced and applied. However, the data is still no 100% clean. I am trying to change all the ‘St’s into ‘Street’ in all the street names. However, St can also be a part of name such as ‘St Clair’ or ‘St George’. Therefore, some names, such as St Geogre St, are difficult to change. Further cleaning is still ongoing. After the project, I learn a lot of interesting facts about Toronto and I have strong confidence on my future project and work.
