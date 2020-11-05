import os

CLIENT_ID = "Enter_the_Application_Id_here" # Application (client) ID of app registration

CLIENT_SECRET = "Enter_the_Client_Secret_Here" # Placeholder - for use ONLY during testing.
# In a production app, we recommend you use a more secure method of storing your secret,
# like Azure Key Vault. Or, use an environment variable as described in Flask's documentation:
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

#AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

REDIRECT_PATH = "/getAToken"  # Used for forming an absolute URL to your redirect URI.
                              # The absolute URL must match the redirect URI you set
                              # in the app's registration in the Azure portal.

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
GRAPH_ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent

BILLING_ENDPOINT = 'https://management.azure.com/subscriptions/REDACTED/providers/Microsoft.Consumption/usageDetails?api-version=2019-10-01'  

#https://stackoverflow.com/questions/63351588/azure-billing-rest-api

#https://docs.microsoft.com/en-us/azure/cost-management-billing/costs/manage-automation

#rateCardUrl = "https://management.azure.com:443/subscriptions/{subscriptionId}/providers/Microsoft.Commerce/RateCard?api-version=2016-08-31-preview&$filter=OfferDurableId eq '{offerId}' and Currency eq '{currencyId}' and Locale eq '{localeId}' and RegionInfo eq '{regionId}'".format(subscriptionId = subscription, offerId = offer, currencyId = currency, localeId = locale, regionId = region)


# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All"]

SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session
