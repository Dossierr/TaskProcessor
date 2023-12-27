import stripe
import time
import subprocess


def bill_tokens(user_ref, tokens_used):
    timestamp=int(time.time())
   
    # Replace SUBSCRIPTION_ITEM_ID with the actual subscription item ID
    subscription_item_id = user_ref

    # Replace sk_test_... with your actual Stripe secret key
    stripe_secret_key = "sk_test_51ORKYaKwogVwbigBrvXVm19oAHbDxpytJk5JFaRzUj1VeuD8BZLTNwfDTkqMJWCPWnkH7EnMGxgKjIpfQ5gFEuXb009mAX7kKC"

    # Set the cURL command
    curl_command = f'curl https://api.stripe.com/v1/subscription_items/{subscription_item_id}/usage_records \
    -u {stripe_secret_key}: \
    -X POST \
    -d quantity={tokens_used} \
    -d timestamp={timestamp} \
    -d action=increment'

    # Run the cURL command using subprocess
    subprocess.run(curl_command, shell=True)