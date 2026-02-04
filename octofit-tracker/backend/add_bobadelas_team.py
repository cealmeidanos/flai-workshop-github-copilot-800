#!/usr/bin/env python
"""Script to add Bobadelas Running Team to the database"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, '/workspaces/flai-workshop-github-copilot-800/octofit-tracker/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import Team

def add_bobadelas_team():
    """Add Bobadelas Running Team to the database"""
    
    # Check if team already exists
    if Team.objects.filter(name='Bobadelas Running Team').exists():
        print('✓ Bobadelas Running Team already exists!')
        team = Team.objects.get(name='Bobadelas Running Team')
        print(f'  - ID: {team.id}')
        print(f'  - Description: {team.description}')
        print(f'  - Created: {team.created_at}')
        return team
    
    # Create the team
    team = Team.objects.create(
        name='Bobadelas Running Team',
        description='Elite runners from Bobadelas committed to excellence and teamwork',
        members=[]
    )
    
    print('✓ Successfully created Bobadelas Running Team!')
    print(f'  - ID: {team.id}')
    print(f'  - Name: {team.name}')
    print(f'  - Description: {team.description}')
    print(f'  - Created: {team.created_at}')
    
    return team

if __name__ == '__main__':
    add_bobadelas_team()
