"""
# Python Inner Classes: Comprehensive In-Depth Guide

This file provides an exhaustive, production-grade guide to mastering
Inner Classes (Nested Classes) in Python. It covers nesting patterns,
accessing outer class data, encapsulation benefits, and real-world uses.

An inner class is a class defined inside another class. It logically
groups related functionality and can enhance encapsulation by scoping
helper classes within their parent.
"""

# --- 0. Setup / Initial State ---
print("=" * 70)
print("  PYTHON INNER CLASSES — COMPREHENSIVE MASTERCLASS")
print("=" * 70)


# =====================================================================
print("\n--- 1. Basic Inner Class Definition ---")
# =====================================================================
# An inner class is simply a class defined inside another class body.
# It is accessed via the outer class name: Outer.Inner

class Outer:
    """Outer class containing an inner class."""

    outer_var = "I belong to Outer"

    class Inner:
        """Inner class nested inside Outer."""
        inner_var = "I belong to Inner"

        def greet(self):
            return f"Hello from Inner! ({self.inner_var})"

# Accessing the inner class through the outer class
inner_obj = Outer.Inner()
print(f"Outer.Inner().greet() -> {inner_obj.greet()}")
print(f"Outer.outer_var       -> {Outer.outer_var}")
print(f"Outer.Inner.inner_var -> {Outer.Inner.inner_var}")
print(f"type(inner_obj)       -> {type(inner_obj)}")


# =====================================================================
print("\n--- 2. Inner Class Cannot Directly Access Outer Class ---")
# =====================================================================
# Unlike Java, Python's inner class does NOT automatically have a
# reference to the outer class. You must pass it explicitly.

class University:
    name = "Python University"

    class Department:
        def __init__(self, dept_name):
            self.dept_name = dept_name

        def info(self):
            # Access outer class attribute via the outer class name
            return f"{self.dept_name} dept at {University.name}"

cs = University.Department("Computer Science")
print(f"cs.info() -> {cs.info()}")


# =====================================================================
print("\n--- 3. Passing Outer Instance to Inner Class ---")
# =====================================================================
# To let the inner class access instance data from the outer class,
# explicitly pass the outer instance.

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.members = []

    def add_member(self, name, role):
        member = self.Member(name, role, self)
        self.members.append(member)
        return member

    def roster(self):
        lines = [f"Team: {self.team_name}"]
        for m in self.members:
            lines.append(f"  - {m}")
        return "\n".join(lines)

    class Member:
        """Inner class that receives a reference to the outer Team."""
        def __init__(self, name, role, team):
            self.name = name
            self.role = role
            self._team = team  # Explicit reference to outer instance

        def team_name(self):
            return self._team.team_name

        def __repr__(self):
            return f"{self.name} ({self.role})"

team = Team("Engineering")
team.add_member("Alice", "Lead")
team.add_member("Bob", "Developer")
team.add_member("Charlie", "QA")
print(team.roster())
print(f"Alice's team: {team.members[0].team_name()}")


# =====================================================================
print("\n--- 4. Multiple Inner Classes ---")
# =====================================================================
# A class can contain multiple inner classes, each serving a
# distinct purpose.

class Computer:
    def __init__(self, brand):
        self.brand = brand
        self.cpu = None
        self.gpu = None

    class CPU:
        def __init__(self, model, cores, clock_ghz):
            self.model = model
            self.cores = cores
            self.clock_ghz = clock_ghz

        def __repr__(self):
            return f"CPU({self.model}, {self.cores}C @ {self.clock_ghz}GHz)"

    class GPU:
        def __init__(self, model, vram_gb):
            self.model = model
            self.vram_gb = vram_gb

        def __repr__(self):
            return f"GPU({self.model}, {self.vram_gb}GB VRAM)"

    def configure(self, cpu_args, gpu_args):
        self.cpu = self.CPU(*cpu_args)
        self.gpu = self.GPU(*gpu_args)
        return self

    def specs(self):
        return f"{self.brand}: {self.cpu} | {self.gpu}"

pc = Computer("Custom Build")
pc.configure(
    cpu_args=("Ryzen 9 7950X", 16, 4.5),
    gpu_args=("RTX 4090", 24)
)
print(f"pc.specs() -> {pc.specs()}")


# =====================================================================
print("\n--- 5. Nested Inner Classes (Multi-Level Nesting) ---")
# =====================================================================
# Inner classes can themselves contain inner classes, though deep
# nesting is generally discouraged for readability.

class Level1:
    name = "Level 1"

    class Level2:
        name = "Level 2"

        class Level3:
            name = "Level 3"

            def where_am_i(self):
                return (f"I'm at {self.name}, inside "
                        f"{Level1.Level2.name}, inside {Level1.name}")

deep = Level1.Level2.Level3()
print(f"deep.where_am_i() -> {deep.where_am_i()}")
print("⚠ Deep nesting is legal but often hurts readability.")


# =====================================================================
print("\n--- 6. Inner Classes for Encapsulation ---")
# =====================================================================
# Inner classes help hide implementation details that are only relevant
# to the outer class, preventing namespace pollution.

class LinkedList:
    """Singly linked list with an encapsulated Node inner class."""

    class _Node:
        """Private inner class — implementation detail of LinkedList."""
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node

        def __repr__(self):
            return f"Node({self.data})"

    def __init__(self):
        self._head = None
        self._size = 0

    def prepend(self, data):
        self._head = self._Node(data, self._head)
        self._size += 1
        return self

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self._head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        items = " -> ".join(str(item) for item in self)
        return f"LinkedList[{items}]"

ll = LinkedList()
ll.prepend(30).prepend(20).prepend(10)
print(f"ll        -> {ll}")
print(f"len(ll)   -> {len(ll)}")
print(f"list(ll)  -> {list(ll)}")


# =====================================================================
print("\n--- 7. Inner Classes as Named Containers / Value Objects ---")
# =====================================================================
# Inner classes are useful for grouping related data that only makes
# sense in the context of the outer class.

class HTTPResponse:
    """HTTP response with inner classes for structured components."""

    class Headers:
        def __init__(self, **kwargs):
            self._headers = {k.lower(): v for k, v in kwargs.items()}

        def get(self, key, default=None):
            return self._headers.get(key.lower(), default)

        def __repr__(self):
            return f"Headers({self._headers})"

    class Body:
        def __init__(self, content, content_type="text/html"):
            self.content = content
            self.content_type = content_type

        @property
        def length(self):
            return len(self.content)

        def __repr__(self):
            preview = self.content[:50] + "..." if len(self.content) > 50 else self.content
            return f"Body({preview!r}, {self.content_type})"

    def __init__(self, status_code, headers_dict, body_content):
        self.status_code = status_code
        self.headers = self.Headers(**headers_dict)
        self.body = self.Body(body_content)

    def __repr__(self):
        return (f"HTTPResponse(status={self.status_code}, "
                f"body_length={self.body.length})")

response = HTTPResponse(
    200,
    {"Content_Type": "application/json", "X_Request_ID": "abc123"},
    '{"message": "Hello, World!", "status": "ok"}'
)

print(f"response              -> {response}")
print(f"response.status_code  -> {response.status_code}")
print(f"response.headers      -> {response.headers}")
print(f"X-Request-ID:         -> {response.headers.get('x_request_id')}")
print(f"response.body         -> {response.body}")
print(f"response.body.length  -> {response.body.length}")


# =====================================================================
print("\n--- 8. Inner Classes with Inheritance ---")
# =====================================================================
# Inner classes can participate in inheritance just like any other class.

class Game:
    class Character:
        def __init__(self, name, hp):
            self.name = name
            self.hp = hp

        def attack(self):
            return f"{self.name} attacks for 10 damage!"

        def __repr__(self):
            return f"{type(self).__name__}({self.name!r}, HP={self.hp})"

    class Warrior(Character):
        def __init__(self, name):
            super().__init__(name, hp=150)

        def attack(self):
            return f"{self.name} swings a sword for 25 damage!"

    class Mage(Character):
        def __init__(self, name):
            super().__init__(name, hp=80)

        def attack(self):
            return f"{self.name} casts fireball for 40 damage!"

warrior = Game.Warrior("Thorin")
mage = Game.Mage("Gandalf")

print(f"warrior -> {warrior}")
print(f"mage    -> {mage}")
print(f"warrior.attack() -> {warrior.attack()}")
print(f"mage.attack()    -> {mage.attack()}")
print(f"isinstance(warrior, Game.Character) -> {isinstance(warrior, Game.Character)}")


# =====================================================================
print("\n--- 9. Factory Pattern with Inner Classes ---")
# =====================================================================
# The outer class can act as a factory that creates inner class instances.

class Logger:
    """Logger with configurable output via inner handler classes."""

    class ConsoleHandler:
        def emit(self, message):
            print(f"    [CONSOLE] {message}")

    class FileHandler:
        def __init__(self, filename):
            self.filename = filename
            self.buffer = []

        def emit(self, message):
            self.buffer.append(message)
            print(f"    [FILE -> {self.filename}] {message}")

    def __init__(self, name, handler_type="console", **kwargs):
        self.name = name
        if handler_type == "console":
            self._handler = self.ConsoleHandler()
        elif handler_type == "file":
            self._handler = self.FileHandler(kwargs.get("filename", "app.log"))
        else:
            raise ValueError(f"Unknown handler type: {handler_type}")

    def log(self, level, message):
        self._handler.emit(f"[{level.upper()}] {self.name}: {message}")

console_log = Logger("AppLogger")
file_log = Logger("DataLogger", handler_type="file", filename="data.log")

console_log.log("info", "Application started")
console_log.log("warn", "Memory usage high")
file_log.log("error", "Database connection failed")
print(f"File handler buffer: {file_log._handler.buffer}")


# =====================================================================
print("\n--- 10. Real-World Example: State Machine ---")
# =====================================================================

class OrderStateMachine:
    """Order processing state machine using inner classes for states."""

    class State:
        """Base state."""
        name = "base"
        def handle(self, order):
            raise NotImplementedError

    class PendingState(State):
        name = "pending"
        def handle(self, order):
            print(f"  Order #{order.order_id}: Processing payment...")
            order._state = OrderStateMachine.PaidState()

    class PaidState(State):
        name = "paid"
        def handle(self, order):
            print(f"  Order #{order.order_id}: Shipping items...")
            order._state = OrderStateMachine.ShippedState()

    class ShippedState(State):
        name = "shipped"
        def handle(self, order):
            print(f"  Order #{order.order_id}: Delivered!")
            order._state = OrderStateMachine.DeliveredState()

    class DeliveredState(State):
        name = "delivered"
        def handle(self, order):
            print(f"  Order #{order.order_id}: Already delivered. No action.")

    def __init__(self, order_id):
        self.order_id = order_id
        self._state = self.PendingState()

    @property
    def status(self):
        return self._state.name

    def advance(self):
        self._state.handle(self)

    def __repr__(self):
        return f"Order(#{self.order_id}, status={self.status})"

order = OrderStateMachine("A100")
print(f"Initial: {order}")

for _ in range(4):
    order.advance()
    print(f"  Current: {order}")


print("\n" + "=" * 70)
print("  End of Python Inner Classes Explanation")
print("=" * 70)
