from supabase import create_client, Client

SUPABASE_URL = "https://dvsekuauqxxxvhqbbhhh.supabase.co" # Replace with your Supabase URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR2c2VrdWF1cXh4eHZocWJiaGhoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzY0MTM5ODEsImV4cCI6MjA1MTk4OTk4MX0.EVlQ7KSSiDkGdqdjvq5yOUCO-KNoPCUssSY5VJMFgh4" # Replace with your Supabase API key

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Step 1: Create a storage bucket
bucket_name = "imgs2" # Name of the bucket to be created
try:
    response = supabase.storage.create_bucket(bucket_name,   
    options={
        "public": True, # Make the bucket public
        "allowed_mime_types": ["image/png"], # Allow only PNG images
        "file_size_limit": 1024*1024, # Limit file size to 1MB
    }
    )
    print(f"Bucket '{bucket_name}' created successfully.")
except Exception as e:
    print(f"Bucket creation error: {e}")