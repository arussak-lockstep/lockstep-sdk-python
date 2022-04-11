#
# Lockstep Platform SDK for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

@dataclass
class CurrencyModel:
    """
    Represents an ISO-4217 currency code definition
    """

    alphaCode: str | None = None
    numericCode: str | None = None
    currencyName: str | None = None
    minorUnit: int | None = None
    symbol: str | None = None

