*** Settings ***
Resource    ./hooks.robot
Resource    ../keywords/login_kw.robot
Resource    ../keywords/invoice_kw.robot
Resource    ../keywords/home_kw.robot
Library     ../lib/config.py
Library     PageObjectLibrary
Library     SeleniumLibrary
Library     DebugLibrary