import re

JOBS_FOLDER = 'G:/Estate Agents'  # location of job folders
CACHE = 'G:/Imports'  # location of local cache
PREFIX = (
    r'1\d{9}KA',  # Key Agent
    r'1\d{9}TM',  # Taylor made
    r'1\d{9}BS',  # Bespoke
    r'HSS\d{3}'  # House simple
)  # list of job folder prefixes
IN_PROGRESS_FOLDER = (  # one entry for each prefix
    'G:/Estate Agents/Key Agent In Progress',  # Key Agent
    'G:/Estate Agents/Taylor Made In Progress',  # Taylor made
    'G:/Estate Agents/Bespoke In Progress',  # Bespoke
    'G:/Estate Agents/House Simple In Progress'  # House simple
)

# TODO create named tuples of all the data for each agent e.g:
AGENT_DATA = (
(PREFIX,IN_PROGRESS_FOLDER),
(PREFIX,IN_PROGRESS_FOLDER),
(PREFIX,IN_PROGRESS_FOLDER),
)
