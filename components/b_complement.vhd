library ieee;
library work;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity b_complement is 
    port(
        cmp_ip : in std_logic_vector(15 downto 0);
        cmp_op : out std_logic_vector(15 downto 0)
         );
end b_complement;

architecture working of b_complement is
    begin
        complement_process: process(cmp_ip)
        begin
            cmp_op <= cmp_ip NAND x"FFFF";
        end process;
end working;