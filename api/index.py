from http.server import BaseHTTPRequestHandler
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the HTML form for GET requests
        try:
            # Read the HTML file
            html_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'index.html')
            with open(html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html_content.encode('utf-8'))
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(f"Error loading page: {str(e)}".encode('utf-8'))
    
    def do_OPTIONS(self):
        # Handle CORS preflight
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Access-Control-Max-Age', '3600')
        self.end_headers()

    def do_POST(self):
        try:
            # Read request body
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            request_json = json.loads(body.decode('utf-8'))
            
            # Extract GAD-7 scores
            scores = []
            for i in range(1, 8):
                key = f'q{i}'
                if key not in request_json:
                    self._send_error(400, f"Missing field: {key}")
                    return
                scores.append(int(request_json[key]))
            
            # Calculate total score
            total_score = sum(scores)
            
            # Classification logic
            classification = "Low"
            if total_score >= 15:
                classification = "High"
            elif total_score >= 10:
                classification = "Moderate"
            
            # Log response time if provided
            response_time = request_json.get('response_time', 'N/A')
            print(f"Processed request. Score: {total_score}, Class: {classification}, Time: {response_time}")
            
            # Send successful response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = json.dumps({
                "score": total_score,
                "classification": classification
            })
            self.wfile.write(response.encode('utf-8'))
            
        except json.JSONDecodeError:
            self._send_error(400, "Invalid JSON")
        except Exception as e:
            self._send_error(500, str(e))
    
    def _send_error(self, code, message):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        error = json.dumps({"error": message})
        self.wfile.write(error.encode('utf-8'))
