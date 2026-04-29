-- =============================================
-- PROCEDURE 1: Upsert contact (insert if new, update if exists)
-- =============================================
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;

-- =============================================
-- PROCEDURE 2: Bulk insert contacts with phone validation
-- =============================================
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    IN p_names TEXT[],
    IN p_phones TEXT[],
    OUT invalid_data TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    current_name TEXT;
    current_phone TEXT;
BEGIN
    invalid_data := ARRAY[]::TEXT[];

    FOR i IN 1..array_length(p_names, 1) LOOP
        current_name := p_names[i];
        current_phone := p_phones[i];

        -- Validate phone number (10-15 digits only)
        IF current_phone !~ '^[0-9]{10,15}$' THEN
            invalid_data := array_append(invalid_data,
                'Name: ' || current_name || ' | Invalid Phone: ' || current_phone);
            CONTINUE;
        END IF;

        -- Insert contact, skip duplicates
        BEGIN
            INSERT INTO contacts(name, phone) VALUES(current_name, current_phone);
        EXCEPTION
            WHEN unique_violation THEN
                CONTINUE;
        END;
    END LOOP;
END;
$$;

-- =============================================
-- PROCEDURE 3: Delete contact by name OR phone
-- =============================================
CREATE OR REPLACE PROCEDURE delete_contact(p_keyword VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_keyword OR phone = p_keyword;
END;
$$;