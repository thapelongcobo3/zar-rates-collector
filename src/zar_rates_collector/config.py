import argparse


class ConfigError(Exception):
    """Raised when the user's configuration is invalid."""


def load_config(argv=None):
    """Return {"base": str, "targets": list[str]} from command-line args."""
    parser = argparse.ArgumentParser(description="Collect daily exchange rates.")
    
    # 1. Add --base and --targets arguments
    parser.add_argument("--base", default="ZAR", help="Base currency (default: ZAR)")
    parser.add_argument("--targets", nargs="+", default=["USD", "EUR", "GBP"], help="Target currencies")

    args = parser.parse_args(argv)

    # 2. Uppercase the base and every target
    base = args.base.upper()
    targets = [t.upper() for t in args.targets]

    # 3. Validate that every code is exactly 3 letters and alphabetic
    all_codes = [base] + targets
    for code in all_codes:
        if not (len(code) == 3 and code.isalpha()):
            raise ConfigError(f"Invalid currency code '{code}': must be exactly 3 alphabetic characters.")

    # 4. Raise ConfigError if base appears in targets
    if base in targets:
        raise ConfigError(f"Base currency '{base}' cannot appear in target currencies.")

    # 5. Return the configuration dictionary
    return {"base": base, "targets": targets}