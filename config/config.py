from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=[
        './toml/settings.toml',
        './toml/.secrets.toml'
    ],
    load_dotenv=True,
    envvar_prefix=False
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
