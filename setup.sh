#!/bin/bash

# TechTell News Agent Repository Setup Script
# This script demonstrates the git commands needed to set up the repository

echo "Setting up TechTell News Agent repository..."

# Add remote origin (replace <your-username> with your actual GitHub username)
echo "Adding remote origin..."
git remote add origin https://github.com/<your-username>/TecTell-News-Agent.git

# Rename current branch to main
echo "Setting main branch..."
git branch -M main

# Push to origin and set upstream
echo "Pushing to origin..."
git push -u origin main

echo "Repository setup complete!"
echo ""
echo "Note: Make sure to replace <your-username> with your actual GitHub username"
echo "Example: git remote add origin https://github.com/yourusername/TecTell-News-Agent.git"