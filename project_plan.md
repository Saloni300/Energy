# ERD
1. User (id, name, email, phone, department_id, city, state)
2. Department (id, name, email, phone)
3. Purchase
   1. EVPurchase (id, user_id, vehicle_make, vehicle_model, ev_type, chassis_number, invoice_number, invoice_image, cost, verification_state[pending, verified, rejected])
   2. ev_type - Dropdown
      - battery electric vehicle
      - hybrid electric vehicle
      - plugin hybrid electric vehicle
4. Rewards (id, name, min_cost, max_cost, points)   # for admins
5. UserRewardPoints (id, user_id, reward_id, points)    # what is associated to user

# Use Cases
## User
1. Login into the app
2. Purchase
   1. View Purchase history
   2. Register new purchase (EV)
      1. Select type of purchase - EV / Solar / Appliance
      2. User fills corresponding form fields and upload the invoice_image
      3. This creates a new EVPurchase record with verification_state as `pending`.
3. UserRewardPoints
   1. Current reward status, how many reward points do they have.
   2. View rewards history
   3. Reward points are given to users based on their activities.
   4. There points can later be redeemed into other entities like 2000points for a 500INR Amazon voucher (Voucher claim is out of scope for now)

## Admin
1. Login to admin app
2. Users
   1. View Users
3. Rewards
   1. View rewards
   2. Create rewards based on specific cost bracket of EVPurchase
4. EVPurchases
   1. View EVPurchases
   2. Approve or Reject pending EVPurchase records
   3. If approved, based on EVPurchase.cost, in which bracket it falls, appropritate UserRewardPoints will be disbursed for User.