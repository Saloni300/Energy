# eneg42
Problem statement ENEG42 for TEAM ALPHA PACT (UIA 407)

## Schema
1. Appliance purchase
   1. Appliance (id, name, billnumber, bill_image, consumption_rating, price, state(pending_verification/verified,rejected))
   2. Bill number to verify the purchase
   3. consumption_rating Out of 5, higher is better
   4. Price to assess the purchasing power of the common people
   5. new record -> pending_verification, not qualify verification process -> rejected, qualify verification process -> verified
   6. Send rewards to verified records' users

2. EV Purchase
   1. EV Purchase (id, name, ev_type, billnumber, bill_image, price, state(pending_verification/verified,rejected))
   2. ev_type - battery electric vehicle, hybrid electric vehicle, plugin hybrid electric vehicle, Fuel cell electric vehicle

3. Solar power generation setup
   1. Solar puchase (id, authorised_seller_id, authorised_seller_name, capacity(kW), billnumber, bill_image, cost, area,power_per_area_of_pannel, direction_degree(efficiency) ,state(pending_verification/verified,rejected))

4. PNG Connection
   1. PNG Connection (id, authorised_operator_id, authorised_operator_name, billnumber, bill_image, cost, state(pending_verification/verified,rejected), address,)

5. PNG Consumption
   1. Based on consumer_id, get data from associated provider
   2. Fetched montly by a microservice (run everyday 12NOON)
   3. PNG Consumption (id, png_connection_id, user_id, month, year, usage_units, bill_amount)
   
6. Electricity consumption
   1. Electricity_Consuption(id, consumer_name,)

## Contributors
1. Tushar
2. Lamisi
