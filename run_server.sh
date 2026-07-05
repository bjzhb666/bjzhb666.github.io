#!/bin/bash
eval "$(/opt/homebrew/bin/brew shellenv)" 2>/dev/null
eval "$(rbenv init - bash)" 2>/dev/null
bundle exec jekyll server --host 127.0.0.1 --port 8820
