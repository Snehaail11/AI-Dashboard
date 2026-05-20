import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# Date range (last 90 days)
dates = pd.date_range(end=datetime.today(), periods=90, freq='D')

# User base
users = []
for u in range(5000):
    plan = np.random.choice(['Free', 'Pro', 'Enterprise'], p=[0.7, 0.25, 0.05])
    signup_date = np.random.choice(dates[:60])
    churn_date = None
    if np.random.random() < 0.15:
        churn_date = signup_date + timedelta(days=np.random.randint(7, 60))
    users.append({'user_id': u, 'plan': plan, 'signup_date': signup_date, 'churn_date': churn_date})

users_df = pd.DataFrame(users)
# Save users data
users_df.to_csv('saas_users.csv', index=False)

# Daily activity
records = []
for date in dates:
    active_users = users_df[(users_df['signup_date'] <= date) &
                            ((users_df['churn_date'].isna()) | (users_df['churn_date'] > date))]
    for _, user in active_users.iterrows():
        # Daily usage
        sessions = np.random.poisson(2 if user['plan'] != 'Free' else 1)
        if sessions == 0:
            continue

        features_used = []
        if np.random.random() < 0.7:
            features_used.append('Dashboard')
        if np.random.random() < 0.5 and user['plan'] != 'Free':
            features_used.append('Reports')
        if np.random.random() < 0.3 and user['plan'] == 'Enterprise':
            features_used.append('AI Assistant')
        if np.random.random() < 0.2:
            features_used.append('API')

        records.append({
            'date': date,
            'user_id': user['user_id'],
            'plan': user['plan'],
            'sessions': sessions,
            'features_used': ','.join(features_used) if features_used else 'None'
        })

df = pd.DataFrame(records)
df.to_csv('saas_product_data.csv', index=False)
print("Generated {} daily activity records".format(len(df)))
print("Generated {} user records".format(len(users_df)))