#!/usr/bin/env python

try:
  from urllib.request import urlopen
except ImportError:
  from urllib2 import urlopen

import json, textwrap

class TextStyles:
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'

def get_status_info():
  try:
    response = urlopen('https://www.githubstatus.com/api/v2/summary.json')
    data = response.read().decode("utf-8")
    return json.loads(data)
  except Exception as e:
    print(e)
    print(TextStyles.FAIL + '[ERROR] Unable to load GitHub status information.' + TextStyles.ENDC)
    quit()

def formatted_status(status):
  status_summary = status['description']

  if status['indicator'] == 'minor':
    status_summary = TextStyles.WARNING + status_summary + ' (Minor Outage)' + TextStyles.ENDC
  elif status['indicator'] == 'major':
    status_summary = TextStyles.FAIL + status_summary + ' (Major Outage)' + TextStyles.ENDC
  elif status['indicator'] == 'critical':
    status_summary = TextStyles.FAIL + status_summary + ' (Critical Outage)' + TextStyles.ENDC
  else:
    status_summary = TextStyles.OKGREEN + status_summary + TextStyles.ENDC

  return status_summary

def formatted_component_status(status):
  if status == 'operational':
    return TextStyles.OKGREEN + status + TextStyles.ENDC
  elif status == 'degraded_performance':
    return TextStyles.WARNING + status + TextStyles.ENDC
  elif status == 'partial_outage':
    return TextStyles.FAIL + status + TextStyles.ENDC
  elif status == 'major_outage':
    return TextStyles.FAIL + status + TextStyles.ENDC

def formatted_incident_impact(impact):
  if impact == 'minor':
    return TextStyles.WARNING + impact + TextStyles.ENDC
  elif impact == 'major':
    return TextStyles.FAIL + impact + TextStyles.ENDC
  elif impact == 'critical':
    return TextStyles.FAIL + impact + TextStyles.ENDC
  else:
    return TextStyles.OKGREEN + impact + TextStyles.ENDC

def formatted_incident_status(incident):
    label = incident['status']
    uri = incident['shortlink']
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST 
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)

def print_components(status_info):
  print('\n----------------------------------------------------------------------------------------')
  print('| {: ^50} | {: ^31} |'.format('COMPONENT', 'STATUS'))
  print('----------------------------------------------------------------------------------------')

  for index, component in enumerate(status_info['components']):
    if component['name'].startswith('Visit www'):
      continue

    print('| {: <50} | {: ^40} |'.format(component['name'], formatted_component_status(component['status'])))

  print('----------------------------------------------------------------------------------------')

def print_incidents(status_info):
  print('\n----------------------------------------------------------------------------------------')
  print('| {: ^50} | {: ^8} | {: ^20} |'.format('INCIDENT', 'IMPACT', 'STATUS'))
  print('----------------------------------------------------------------------------------------')

  for index, incident in enumerate(status_info['incidents']):
    if index > 0:
      print('|......................................................................................|')

    wrapped_name = textwrap.wrap(incident['name'], width=50)

    for index, name_line in enumerate(wrapped_name):
      if index == 0:
        print('| {: <50} | {: ^17} | {: ^63} |'.format(name_line, formatted_incident_impact(incident['impact']), formatted_incident_status(incident)))
      else:
        print('| {: <50} | {: ^17} | {: ^20} |'.format(name_line, formatted_incident_impact(' '), ''))

  if len(status_info['incidents']) == 0:
    print('| {: ^92} |'.format(TextStyles.BOLD + 'There are currently no active incidents.' + TextStyles.ENDC))

  print('----------------------------------------------------------------------------------------')

def get_status():
  status_info = get_status_info()

  print('----------------------------------------------------------------------------------------')
  print('| {: ^101} |'.format(TextStyles.BOLD + 'GitHub Status: ' + TextStyles.ENDC + formatted_status(status_info['status'])))
  print('----------------------------------------------------------------------------------------')

  print_components(status_info)
  print_incidents(status_info)
