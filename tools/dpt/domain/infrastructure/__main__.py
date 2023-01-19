import pulumi_snowflake as snowflake

simple = snowflake.Database("simple",
        comment="test comment",
        data_retention_time_in_days=1)