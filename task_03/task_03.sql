-- postgresql

-- DROP SCHEMA IF EXISTS assignment ;
CREATE SCHEMA IF NOT EXISTS assignment;


-- DROP TABLE IF EXISTS assignment.product;
CREATE TABLE IF NOT EXISTS assignment.product
(
    id serial4 NOT NULL,
    title character varying(256) COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default",
    price double precision NOT NULL,
    product_images json,
    category character varying(128) COLLATE pg_catalog."default",
    is_promoted boolean,
    CONSTRAINT product_pkey PRIMARY KEY (id)
)

-- DROP TABLE IF EXISTS assignment.stores;
CREATE TABLE IF NOT EXISTS assignment.stores
(
    id serial4 NOT NULL,
    name character varying(256) COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default",
    address text,
    region text,
    CONSTRAINT stores_pkey PRIMARY KEY (id)
)

-- DROP TABLE IF EXISTS assignment.inventory;
-- NOTE: inventory will record products and store/warehouse which belongs to that products.
CREATE TABLE IF NOT EXISTS assignment.inventory
(
    id serial4 NOT NULL,
    store_id integer NOT NULL,
    product_id integer NOT NULL,
    available_date timestamp with time zone,
    stock_quantity integer NOT NULL DEFAULT 0,
    CONSTRAINT inventory_pkey PRIMARY KEY (id),
    CONSTRAINT fk_product_id FOREIGN KEY (product_id)
        REFERENCES assignment.product (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fk_store_id FOREIGN KEY (store_id)
        REFERENCES assignment.stores (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)