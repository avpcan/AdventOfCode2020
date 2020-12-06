from pydantic import BaseModel, ValidationError, validator
from typing import Optional
from re import match


class SneakyPassport(BaseModel):
    """A passport model with optional cid, in order to accept North Pole Passes"""

    byr: int
    iyr: int
    eyr: int
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: Optional[int]


class ExtraValidPassport(BaseModel):
    """A passport model with optional cid, in order to accept North Pole Passes"""

    byr: int
    iyr: int
    eyr: int
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: Optional[int]

    @validator("byr")
    def validate_byr(cls, v):
        if v < 1920 or v > 2002:
            raise ValueError("Invalid birth year")

    @validator("iyr")
    def validate_iyr(cls, v):
        if v < 2010 or v > 2020:
            raise ValueError("Invalid issue year")

    @validator("eyr")
    def validate_eyr(cls, v):
        if v < 2020 or v > 2030:
            raise ValueError("Invalid expiry year")

    @validator("hgt")
    def validate_hgt(cls, v):
        unit = v[-2:]
        value = int(v[:-2])
        if unit == "in":
            if value < 59 or value > 76:
                raise ValueError("Invalid height in inches")
        elif unit == "cm":
            if value < 150 or value > 193:
                raise ValueError("Invalid height in centimeters")
        else:
            raise ValueError("Invalid unit for height")

    @validator("hcl")
    def validate_hcl(cls, v):
        pattern = "^#[0-9, a-f]{6}$"
        if not match(pattern, v):
            raise ValueError(
                "Invalid hair colour format; must be a # followed by exactly six "
                "characters 0-9 or a-f."
            )

    @validator("ecl")
    def validate_ecl(cls, v):
        valid_ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if v not in valid_ecls:
            raise ValueError(
                "Invalid eye colour format; must be one of: amb blu brn gry grn hzl oth."
            )

    @validator("pid")
    def validate_pid(cls, v):
        pattern = "^[0-9]{9}$"
        if not match(pattern, v):
            raise ValueError(
                "Invalid passport id; must be a 9-digit number, including leading 0s."
            )
