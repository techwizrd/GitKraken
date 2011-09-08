#!/usr/bin/python

from GitKraken.gtk.project_manager import ProjectManager

def main():
    """Starts the actual GitKraken application"""
    project_manager = ProjectManager()
    project_manager.main()

if __name__ == '__main__':
    main()
