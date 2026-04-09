#!/bin/bash

set -e

systemctl restart httpd
systemctl enable httpd