library ieee;
library work;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity sign_7_extender is 
    port(
        se_ip_7 : in std_logic_vector(8 downto 0);
        se_op_7 : out std_logic_vector(15 downto 0)
        );
end sign_7_extender;

architecture working of sign_7_extender is
    begin
        sign_7_extender_process: process(se_ip_7)
        variable temp : integer;
        begin
            temp := to_integer(unsigned(se_ip_7));
            se_op_7 <= std_logic_vector(to_unsigned(temp,16));
        end process;
end working;