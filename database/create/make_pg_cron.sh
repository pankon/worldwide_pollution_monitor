git clone https://github.com/citusdata/pg_cron.git
cd pg_cron
# Ensure pg_config is in your path, e.g.
export PATH=/usr/pgsql-9.6/bin:$PATH
make && sudo PATH=$PATH make install

find C:\ 'postgresql.conf'
