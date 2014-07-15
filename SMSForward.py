#!/usr/bin/python

import argparse

import providers


def main():
    parser = argparse.ArgumentParser(description="Forward the given text as SMS to the right user")
    parser.add_argument('-p', '--provider', required=True, help='The provider name')
    parser.add_argument('-u', '--user', required=True, help='The user name')
    parser.add_argument('-t', '--token', required=True, help='The user token')
    parser.add_argument('-m', '--message', required=True, help='The message to forward')

    options = parser.parse_args()

    # Open the right provider
    provider = providers.create(options.provider, {'user': options.user, 'token': options.token})
    provider.send_message(options.message)

if __name__ == '__main__':
    main()
