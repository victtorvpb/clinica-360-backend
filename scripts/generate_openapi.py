#!/usr/bin/env python3
"""
Generate OpenAPI/Swagger JSON file
Run: python scripts/generate_openapi.py
"""

import json
import sys
import os

# Add root directory to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.main import app

def generate_openapi():
    """Generate OpenAPI JSON file"""
    print("🔧 Generating OpenAPI specification...")
    
    try:
        # Get OpenAPI schema
        openapi_schema = app.openapi()
        
        # Write to file
        with open("openapi.json", "w", encoding="utf-8") as f:
            json.dump(openapi_schema, f, indent=2, ensure_ascii=False)
        
        print("✅ OpenAPI specification generated: openapi.json")
        print(f"📊 Found {len(openapi_schema.get('paths', {}))} endpoints")
        
        # Show some stats
        tags = set()
        methods = []
        
        for path, path_data in openapi_schema.get('paths', {}).items():
            for method, operation in path_data.items():
                if method != 'parameters':
                    methods.append(method.upper())
                    if 'tags' in operation:
                        tags.update(operation['tags'])
        
        print(f"🏷️  Tags: {', '.join(sorted(tags))}")
        print(f"📋 Methods: {', '.join(set(methods))}")
        
        print("\n🌐 Access Swagger UI at:")
        print("   - http://localhost:8000/docs")
        print("   - http://localhost:8000/redoc")
        
    except Exception as e:
        print(f"❌ Error generating OpenAPI: {e}")
        sys.exit(1)

if __name__ == "__main__":
    generate_openapi() 
