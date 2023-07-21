library ieee;
library work;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity comparator is 
    port(
        comp_ip_1 : in std_logic_vector(15 downto 0);
        comp_ip_2: in std_logic_vector(15 downto 0);
        ltout : out std_logic;
        eout : out std_logic 
        );
end comparator;

architecture working of comparator is
    begin
        comparator_process: process(comp_ip_1,comp_ip_2)
        begin
            if comp_ip_1 < comp_ip_2 then
                ltout <= '1';
            else
                ltout <= '0';
            end if;
            if comp_ip_1 = comp_ip_2 then
                eout  <= '1';
            else
                eout  <= '0';
            end if;
        end process;
end working;