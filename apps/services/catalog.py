from dataclasses import dataclass


@dataclass(frozen=True)
class DBMS:
    slug: str 
    label: str
    description: str


@dataclass(frozen=True)
class Runtime:
    slug: str  
    label: str
    description: str


DATABASES: tuple[DBMS, ...] = (
    DBMS(
        'postgres',
        'PostgreSQL',
        'The PostgreSQL object-relational database system provides reliability and data integrity',
    ),
    DBMS(
        'mysql',
        'MySQL',
        'MySQL is a widely used, open-source relational database management system (RDBMS).',
    ),
    DBMS(
        'mongodb',
        'MongoDB',
        'MongoDB document databases provide high availability and easy scalability.',
    ),
    DBMS(
        'redis',
        'Redis',
        "Redis is the world's fastest data platform for caching, vector search, and NoSQL databases.",
    ),
)

RUNTIMES: tuple[Runtime, ...] = (
    Runtime(
        'python',
        'Python',
        'Python is an interpreted, interactive, object-oriented, open-source programming language.',
    ),
    Runtime(
        'nodejs',
        'Node.js',
        'Node.js is a JavaScript-based platform for server-side and networking applications',
    ),
)
