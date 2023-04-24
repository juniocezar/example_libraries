def sso(username, token, user_account = None):
    from databricks.sdk.runtime import sc

    prep_user_account = user_account
    if prep_user_account is not None:
        prep_user_account = f":{user_account}"
    sc._jsc.hadoopConfiguration().set('fs.s3a.access.key', f"{username}:{token}{prep_user_account}")
    sc._jsc.hadoopConfiguration().set('fs.s3a.secret.key', 'none')
    sc._jsc.hadoopConfiguration().set("fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.BasicAWSCredentialsProvider")