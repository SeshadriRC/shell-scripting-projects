#!/usr/bin/env python3
"""
generate_logs.py
Generates realistic application, web server, authentication, database,
and structured JSON log files for shell scripting exercises.
"""

import os
import random
import gzip
import time
from datetime import datetime, timedelta

LOG_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_DIR = os.path.join(LOG_DIR, "archive")
os.makedirs(ARCHIVE_DIR, exist_ok=True)

# Fixed base time for reproducible yet realistic logs (around Oct 22, 2026)
NOW = datetime(2026, 10, 22, 10, 30, 0)

# --- 1. Generate Web Server Access Log (Combined Log Format) ---
def generate_access_log():
    filepath = os.path.join(LOG_DIR, "access.log")
    print(f"Generating {filepath}...")

    ips = [
        ("192.168.1.45", 250),     # Internal office IP (heavy)
        ("192.168.1.102", 180),    # Internal developer
        ("10.0.2.15", 120),        # Internal microservice
        ("203.0.113.195", 420),    # Aggressive crawler / scraper
        ("198.51.100.88", 150),    # Regular customer
        ("198.51.100.14", 95),     # Mobile app user
        ("45.33.32.156", 75),      # Scanner / vulnerability probe
        ("185.220.101.5", 60),     # Tor exit node / probe
        ("66.249.66.1", 110),      # Googlebot
        ("157.55.39.1", 85),       # Bingbot
        ("172.16.0.22", 40),       # QA team
        ("93.184.216.34", 30),     # Normal visitor
        ("140.82.112.4", 25),      # Webhook callback
    ]
    ip_pool = []
    for ip, count in ips:
        ip_pool.extend([ip] * count)

    endpoints = [
        ("GET", "/api/v1/products", 200, 3500, 0.40),
        ("GET", "/api/v1/products/featured", 200, 1850, 0.15),
        ("POST", "/api/v1/cart/items", 201, 412, 0.08),
        ("GET", "/api/v1/cart", 200, 890, 0.07),
        ("POST", "/api/v1/checkout", 200, 1240, 0.04),
        ("POST", "/api/v1/checkout", 500, 245, 0.02),
        ("POST", "/api/v1/checkout", 504, 180, 0.01),
        ("GET", "/api/v1/orders/my-orders", 200, 2150, 0.05),
        ("GET", "/api/v1/orders/99999", 404, 134, 0.03),
        ("GET", "/login", 200, 4200, 0.04),
        ("POST", "/api/v1/auth/login", 200, 520, 0.03),
        ("POST", "/api/v1/auth/login", 401, 160, 0.03),
        ("GET", "/static/css/main.bundle.css", 200, 84200, 0.02),
        ("GET", "/static/js/app.bundle.js", 200, 320450, 0.02),
        ("GET", "/health", 200, 24, 0.05),
        ("GET", "/metrics", 200, 15400, 0.02),
        ("GET", "/wp-login.php", 404, 162, 0.015),
        ("GET", "/.env", 403, 153, 0.01),
        ("GET", "/admin/config.php", 404, 162, 0.008),
        ("GET", "/phpmyadmin", 404, 162, 0.008),
        ("GET", "/api/v2/reports/export", 502, 340, 0.005),
    ]

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
        "curl/8.5.0",
        "python-requests/2.31.0",
        "Go-http-client/1.1",
    ]

    referrers = [
        "https://www.google.com/",
        "https://example.com/",
        "https://example.com/products",
        "https://example.com/checkout",
        "-",
    ]

    total_records = len(ip_pool)
    start_time = NOW - timedelta(hours=24)
    time_step = timedelta(seconds=(24 * 3600) // total_records)

    lines = []
    current_time = start_time
    for i in range(total_records):
        ip = random.choice(ip_pool)
        ep = random.choices(endpoints, weights=[e[4] for e in endpoints])[0]
        method, path, status, base_bytes, _ = ep
        byte_size = max(50, base_bytes + random.randint(-50, 100)) if status < 400 else base_bytes
        user = "-" if ip.startswith("10.") or "bot" in ip else random.choice(["-", "-", "-", "sesha", "admin", "alice"])
        ua = random.choice(user_agents)
        ref = random.choice(referrers)

        # Apache/Nginx combined: IP - user [datetime +0000] "METHOD /path HTTP/1.1" status bytes "ref" "ua"
        time_str = current_time.strftime("%d/%b/%Y:%H:%M:%S +0000")
        line = f'{ip} - {user} [{time_str}] "{method} {path} HTTP/1.1" {status} {byte_size} "{ref}" "{ua}"\n'
        lines.append(line)
        current_time += time_step + timedelta(seconds=random.randint(0, 5))

    with open(filepath, "w") as f:
        f.writelines(lines)
    print(f"Written {len(lines)} records to {filepath}")


# --- 2. Generate Application Log (Multi-line Spring Boot / Java style) ---
def generate_app_log():
    filepath = os.path.join(LOG_DIR, "app.log")
    print(f"Generating {filepath}...")

    stack_traces = {
        "NullPointerException": """java.lang.NullPointerException: Cannot invoke "com.example.model.Customer.getAddress()" because "customer" is null
\tat com.example.service.OrderService.validateShippingAddress(OrderService.java:189)
\tat com.example.service.OrderService.processOrder(OrderService.java:94)
\tat com.example.controller.OrderController.submitOrder(OrderController.java:55)
\tat jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:103)
\tat java.lang.reflect.Method.invoke(Method.java:580)
\tat org.springframework.web.method.support.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:255)
\tat org.springframework.web.method.support.InvocableHandlerMethod.invokeForRequest(InvocableHandlerMethod.java:188)""",

        "DatabaseTimeoutException": """org.springframework.dao.QueryTimeoutException: Statement cancelled due to client timeout
\tat org.postgresql.core.v3.QueryExecutorImpl.execute(QueryExecutorImpl.java:345)
\tat org.postgresql.jdbc.PgStatement.executeInternal(PgStatement.java:498)
\tat com.zaxxer.hikari.pool.ProxyStatement.execute(ProxyStatement.java:94)
\tat com.example.repository.InventoryRepository.updateStockBatch(InventoryRepository.java:78)
\tat com.example.service.InventoryService.syncInventory(InventoryService.java:112)
\tat com.example.cron.InventorySyncJob.execute(InventorySyncJob.java:45)""",

        "ConnectionPoolExhausted": """com.zaxxer.hikari.pool.HikariPool$PoolInitializationException: Connection is not available, request timed out after 30005ms (total=50, active=50, idle=0, waiting=14)
\tat com.zaxxer.hikari.pool.HikariPool.throwPoolInitializationException(HikariPool.java:604)
\tat com.zaxxer.hikari.pool.HikariPool.getConnection(HikariPool.java:194)
\tat com.zaxxer.hikari.HikariDataSource.getConnection(HikariDataSource.java:99)
\tat org.hibernate.engine.jdbc.connections.internal.DatasourceConnectionProviderImpl.getConnection(DatasourceConnectionProviderImpl.java:122)""",

        "PaymentGatewayException": """com.example.exception.PaymentGatewayException: Stripe API returned HTTP 504 Gateway Timeout for idempotency_key=idemp_9f82d1c
\tat com.example.gateway.StripeClient.charge(StripeClient.java:142)
\tat com.example.service.PaymentService.processPayment(PaymentService.java:67)
\tat com.example.consumer.OrderKafkaConsumer.onMessage(OrderKafkaConsumer.java:51)
\tat org.springframework.kafka.listener.KafkaMessageListenerContainer$ListenerConsumer.run(KafkaMessageListenerContainer.java:1250)"""
    }

    info_messages = [
        "Started Application in 4.312 seconds (JVM running for 5.12)",
        "User logged in successfully [userId=usr_10291, ip=192.168.1.102]",
        "User logged in successfully [userId=usr_88204, ip=198.51.100.88]",
        "Order #ORD-99120 placed successfully. Total amount: $129.50",
        "Order #ORD-99121 placed successfully. Total amount: $49.99",
        "Order #ORD-99122 placed successfully. Total amount: $899.00",
        "Cache refreshed for key 'catalog:categories:all' (took 14ms)",
        "Webhook notification sent to merchant_id=m_881 with status 200",
        "Kafka partition [orders-topic-0] offset committed at 49102",
        "Daily report aggregation started for date 2026-10-21",
        "Daily report aggregation completed in 3120ms (processed 4812 rows)",
        "Health check status: UP [Disk: 42% free, DB: OK, Redis: OK]",
    ]

    warn_messages = [
        "Slow query detected: SELECT * FROM audit_logs took 2450ms (threshold: 1000ms)",
        "Deprecated API endpoint /api/v1/user/get invoked by client v1.2",
        "High memory utilization detected: 78.4% of heap space in use",
        "Rate limit threshold reached (90/100 req/min) for client_id=c_994",
        "Kafka consumer lag high on partition 2: 1250 messages behind",
        "Failed payment retry attempt 1 of 3 for order #ORD-99125",
    ]

    debug_messages = [
        "Evaluating JWT claims for subject=usr_10291, roles=[ROLE_USER]",
        "Executing SQL: SELECT u1_0.id, u1_0.email FROM users u1_0 WHERE u1_0.email = ?",
        "Redis GET 'session:sess_a1b2c3' returned 184 bytes (cache HIT)",
        "Publishing event OrderCreatedEvent to internal ApplicationEventPublisher",
        "HTTP request payload parsed: 4 fields, content-length=128",
    ]

    lines = []
    current_time = NOW - timedelta(hours=18)

    for i in range(800):
        current_time += timedelta(seconds=random.randint(1, 45), milliseconds=random.randint(10, 990))
        time_str = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        thread = f"http-nio-8080-exec-{random.randint(1, 10)}"
        trace_id = f"trace_{random.randint(100000, 999999)}"

        roll = random.random()
        if roll < 0.65:
            msg = random.choice(info_messages)
            lines.append(f"{time_str} [{thread}] INFO  c.e.service.CoreApplication - [trace_id={trace_id}] {msg}\n")
        elif roll < 0.85:
            msg = random.choice(debug_messages)
            lines.append(f"{time_str} [{thread}] DEBUG c.e.repository.QueryLogger - [trace_id={trace_id}] {msg}\n")
        elif roll < 0.94:
            msg = random.choice(warn_messages)
            lines.append(f"{time_str} [{thread}] WARN  c.e.service.MetricsWatcher - [trace_id={trace_id}] {msg}\n")
        else:
            # ERROR with stack trace!
            err_type = random.choice(list(stack_traces.keys()))
            st = stack_traces[err_type]
            lines.append(f"{time_str} [{thread}] ERROR c.e.controller.GlobalExceptionHandler - [trace_id={trace_id}] Exception occurred while handling request: {err_type}\n")
            lines.append(f"{st}\n")

    with open(filepath, "w") as f:
        f.writelines(lines)
    print(f"Written {len(lines)} log blocks to {filepath}")


# --- 3. Generate JSON Structured Log ---
def generate_json_log():
    import json
    filepath = os.path.join(LOG_DIR, "api-service.json.log")
    print(f"Generating {filepath}...")

    lines = []
    current_time = NOW - timedelta(hours=12)

    services = ["auth-service", "order-service", "payment-service", "inventory-service", "notification-service"]
    levels = ["INFO", "INFO", "INFO", "WARN", "DEBUG", "ERROR"]

    for i in range(600):
        current_time += timedelta(seconds=random.randint(2, 60), milliseconds=random.randint(1, 999))
        lvl = random.choice(levels)
        svc = random.choice(services)
        status_code = 200 if lvl in ["INFO", "DEBUG"] else (400 if lvl == "WARN" else 500)
        
        entry = {
            "timestamp": current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "level": lvl,
            "service": svc,
            "environment": "production",
            "trace_id": f"trace-{random.randint(10000000, 99999999):x}",
            "http": {
                "method": random.choice(["GET", "POST", "PUT", "DELETE"]),
                "route": random.choice(["/users", "/orders", "/payments", "/checkout", "/catalog", "/health"]),
                "status_code": status_code,
                "latency_ms": round(random.uniform(5.5, 450.0), 2)
            },
            "user_id": f"u_{random.randint(1000, 9999)}" if random.random() > 0.3 else None,
            "message": f"Processed request in {svc}" if lvl != "ERROR" else f"Failed to complete transaction in {svc}: database connection failure"
        }
        lines.append(json.dumps(entry) + "\n")

    with open(filepath, "w") as f:
        f.writelines(lines)
    print(f"Written {len(lines)} JSON records to {filepath}")


# --- 4. Generate Linux Auth / SSH Log (auth.log) ---
def generate_auth_log():
    filepath = os.path.join(LOG_DIR, "auth.log")
    print(f"Generating {filepath}...")

    lines = []
    current_time = NOW - timedelta(hours=36)

    # Brute force attacker IPs
    attacker_ip = "185.220.101.5"
    attacker_ip_2 = "203.0.113.195"
    bad_users = ["root", "admin", "test", "oracle", "ubuntu", "guest", "postgres"]

    for i in range(500):
        current_time += timedelta(seconds=random.randint(5, 120))
        time_str = current_time.strftime("%b %d %H:%M:%S")
        pid = random.randint(10000, 32000)

        roll = random.random()
        if roll < 0.40:
            # Brute force failed password attempt
            ip = attacker_ip if random.random() < 0.7 else attacker_ip_2
            u = random.choice(bad_users)
            lines.append(f"{time_str} ubuntu-server sshd[{pid}]: Failed password for invalid user {u} from {ip} port {random.randint(30000, 60000)} ssh2\n")
        elif roll < 0.65:
            # Accepted legitimate login
            u = random.choice(["sesha", "deployer", "developer"])
            lines.append(f"{time_str} ubuntu-server sshd[{pid}]: Accepted publickey for {u} from 192.168.1.102 port {random.randint(40000, 60000)} ssh2: RSA SHA256:7uK+aB8/4rL... \n")
            lines.append(f"{time_str} ubuntu-server systemd-logind[{random.randint(800, 1200)}]: New session {random.randint(20, 90)} of user {u}.\n")
        elif roll < 0.85:
            # Sudo command execution
            cmd = random.choice([
                "/usr/bin/systemctl restart nginx",
                "/usr/bin/apt-get update",
                "/bin/cat /var/log/syslog",
                "/usr/bin/docker ps",
                "/usr/bin/tail -f /var/log/app.log"
            ])
            lines.append(f"{time_str} ubuntu-server sudo:   sesha : TTY=pts/0 ; PWD=/home/sesha ; USER=root ; COMMAND={cmd}\n")
        else:
            # Cron execution or session closed
            lines.append(f"{time_str} ubuntu-server CRON[{pid}]: (root) CMD (/usr/local/bin/logrotate /etc/logrotate.conf > /dev/null 2>&1)\n")

    with open(filepath, "w") as f:
        f.writelines(lines)
    print(f"Written {len(lines)} auth entries to {filepath}")


# --- 5. Generate Database Log (Slow queries, Deadlocks) ---
def generate_db_log():
    filepath = os.path.join(LOG_DIR, "database.log")
    print(f"Generating {filepath}...")

    lines = []
    current_time = NOW - timedelta(hours=20)

    queries = [
        ("SELECT * FROM users WHERE status = 'ACTIVE' ORDER BY created_at DESC LIMIT 50;", 12.4),
        ("SELECT count(*) FROM orders WHERE order_date >= '2026-10-01';", 45.2),
        ("SELECT o.id, c.name, sum(i.price * i.quantity) FROM orders o JOIN customers c ON o.customer_id = c.id JOIN items i ON i.order_id = o.id GROUP BY o.id, c.name ORDER BY sum DESC LIMIT 100;", 4890.5), # SLOW!
        ("SELECT * FROM audit_logs WHERE payload LIKE '%password%' ORDER BY id DESC;", 3420.1), # SLOW!
        ("UPDATE inventory SET stock = stock - 1 WHERE product_id = 4521;", 8.1),
        ("INSERT INTO cart_items (cart_id, item_id, quantity) VALUES (4091, 102, 1);", 5.3),
        ("SELECT pg_stat_activity.* FROM pg_stat_activity WHERE state != 'idle';", 18.0),
    ]

    for i in range(400):
        current_time += timedelta(seconds=random.randint(10, 150), milliseconds=random.randint(100, 900))
        time_str = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        pid = random.randint(12000, 18000)

        q, base_dur = random.choice(queries)
        dur = round(base_dur + random.uniform(-2.0, 15.0), 3)

        if dur > 1000.0:
            lines.append(f"{time_str} UTC [{pid}] LOG:  duration: {dur} ms  statement: {q}\n")
            lines.append(f"{time_str} UTC [{pid}] WARNING:  query execution time exceeded 1000ms threshold\n")
        elif random.random() < 0.03:
            lines.append(f"{time_str} UTC [{pid}] ERROR:  deadlock detected\n")
            lines.append(f"{time_str} UTC [{pid}] DETAIL:  Process {pid} waits for ShareLock on transaction 891283; blocked by process {pid+1}.\n")
        else:
            lines.append(f"{time_str} UTC [{pid}] LOG:  duration: {dur} ms  statement: {q}\n")

    with open(filepath, "w") as f:
        f.writelines(lines)
    print(f"Written {len(lines)} database entries to {filepath}")


# --- 6. Generate Archived / Rotated Logs ---
def generate_archives():
    print(f"Generating archived files in {ARCHIVE_DIR}...")
    
    # 1. Rotated gzipped access log from 7 days ago
    for days_ago in [7, 5, 3]:
        date_str = (NOW - timedelta(days=days_ago)).strftime("%Y-%m-%d")
        gz_path = os.path.join(ARCHIVE_DIR, f"access-{date_str}.log.gz")
        dummy_content = f"# Archived access log for {date_str}\n" + "\n".join([
            f'192.168.1.{random.randint(1, 254)} - - [{date_str}:12:00:00 +0000] "GET /api/v1/health HTTP/1.1" 200 24 "-" "curl/7.68.0"'
            for _ in range(200)
        ])
        with gzip.open(gz_path, "wt") as gz_file:
            gz_file.write(dummy_content)
        
        # Set file modification time to days_ago
        mtime = time.time() - (days_ago * 86400)
        os.utime(gz_path, (mtime, mtime))

    # 2. Rotated plain application logs
    for days_ago in [10, 8, 4, 2]:
        date_str = (NOW - timedelta(days=days_ago)).strftime("%Y-%m-%d")
        log_path = os.path.join(ARCHIVE_DIR, f"app-{date_str}.log")
        dummy_content = f"# Archived app log for {date_str}\n" + "\n".join([
            f'{date_str} 00:00:0{i} [main] INFO  c.e.service.CoreApplication - Processed batch run {i}'
            for i in range(150)
        ])
        with open(log_path, "w") as f:
            f.write(dummy_content)
        mtime = time.time() - (days_ago * 86400)
        os.utime(log_path, (mtime, mtime))

    print("Archived log files successfully created with realistic modification timestamps.")


if __name__ == "__main__":
    generate_access_log()
    generate_app_log()
    generate_json_log()
    generate_auth_log()
    generate_db_log()
    generate_archives()
    print("\nAll sample logs successfully generated!")
